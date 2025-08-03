#!/usr/bin/env python3
"""
Performance Tracking Script
Monitor CI/CD pipeline performance over time and detect regressions

Created for: Zoom Deep Clean Enhanced
Purpose: Proactive performance monitoring and alerting
"""

import json
import time
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import statistics


class PerformanceTracker:
    """Track and analyze CI/CD pipeline performance metrics"""

    def __init__(self, metrics_file: str = "performance_metrics.json"):
        self.metrics_file = Path(metrics_file)
        self.thresholds = {
            "test_time": 60,  # seconds
            "lint_time": 30,  # seconds
            "security_time": 45,  # seconds
            "total_time": 120,  # seconds
            "alert_threshold": 80,  # percentage of threshold
        }

    def load_metrics(self) -> List[Dict]:
        """Load historical performance metrics"""
        if not self.metrics_file.exists():
            return []

        try:
            with open(self.metrics_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_metrics(self, metrics: List[Dict]) -> None:
        """Save performance metrics to file"""
        self.metrics_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.metrics_file, "w") as f:
            json.dump(metrics, f, indent=2)

    def run_timed_tests(self) -> Dict[str, float]:
        """Run tests and measure execution time"""
        print("🔍 Running performance measurement...")

        results = {}

        # Test execution timing
        start_time = time.time()
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short", "-q"],
                capture_output=True,
                text=True,
                timeout=300,
            )

            test_time = time.time() - start_time
            results["test_time"] = test_time
            results["test_success"] = result.returncode == 0
            results["test_count"] = self._count_tests(result.stdout)

            print(f"✅ Tests completed in {test_time:.1f}s")

        except subprocess.TimeoutExpired:
            results["test_time"] = 300  # timeout value
            results["test_success"] = False
            results["test_count"] = 0
            print("❌ Tests timed out after 300s")

        # Lint timing
        start_time = time.time()
        try:
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "flake8",
                    "zoom_deep_clean",
                    "--count",
                    "--statistics",
                ],
                capture_output=True,
                timeout=60,
            )

            subprocess.run(
                [sys.executable, "-m", "black", "--check", "zoom_deep_clean/"],
                capture_output=True,
                timeout=60,
            )

            lint_time = time.time() - start_time
            results["lint_time"] = lint_time
            print(f"✅ Lint completed in {lint_time:.1f}s")

        except (subprocess.TimeoutExpired, FileNotFoundError):
            results["lint_time"] = 60
            print("⚠️ Lint tools not available or timed out")

        # Security scan timing (if tools available)
        start_time = time.time()
        try:
            subprocess.run(
                [sys.executable, "-m", "bandit", "-r", "zoom_deep_clean/", "-q"],
                capture_output=True,
                timeout=120,
            )

            security_time = time.time() - start_time
            results["security_time"] = security_time
            print(f"✅ Security scan completed in {security_time:.1f}s")

        except (subprocess.TimeoutExpired, FileNotFoundError):
            results["security_time"] = 0  # Not available
            print("⚠️ Security tools not available")

        # Calculate total time
        results["total_time"] = (
            results["test_time"] + results["lint_time"] + results["security_time"]
        )

        return results

    def _count_tests(self, pytest_output: str) -> int:
        """Extract test count from pytest output"""
        try:
            # Look for pattern like "27 passed"
            import re

            match = re.search(r"(\d+) passed", pytest_output)
            return int(match.group(1)) if match else 0
        except:
            return 0

    def analyze_performance(self, current: Dict[str, float]) -> Dict[str, any]:
        """Analyze current performance against thresholds and trends"""
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "current_metrics": current,
            "threshold_analysis": {},
            "trend_analysis": {},
            "alerts": [],
        }

        # Threshold analysis
        for metric, threshold in self.thresholds.items():
            if metric == "alert_threshold":
                continue

            current_value = current.get(metric, 0)
            if current_value > 0:  # Only analyze if we have data
                percentage = (current_value / threshold) * 100

                analysis["threshold_analysis"][metric] = {
                    "current": current_value,
                    "threshold": threshold,
                    "percentage": percentage,
                    "status": self._get_status(percentage),
                }

                # Generate alerts
                if percentage > 100:
                    analysis["alerts"].append(
                        {
                            "level": "ERROR",
                            "metric": metric,
                            "message": f"{metric} exceeded threshold: {current_value:.1f}s > {threshold}s",
                        }
                    )
                elif percentage > self.thresholds["alert_threshold"]:
                    analysis["alerts"].append(
                        {
                            "level": "WARNING",
                            "metric": metric,
                            "message": f"{metric} approaching threshold: {current_value:.1f}s ({percentage:.1f}%)",
                        }
                    )

        # Trend analysis (if we have historical data)
        historical = self.load_metrics()
        if len(historical) >= 3:  # Need at least 3 data points
            analysis["trend_analysis"] = self._analyze_trends(historical, current)

        return analysis

    def _get_status(self, percentage: float) -> str:
        """Get status based on percentage of threshold"""
        if percentage > 100:
            return "FAILED"
        elif percentage > self.thresholds["alert_threshold"]:
            return "WARNING"
        else:
            return "OK"

    def _analyze_trends(self, historical: List[Dict], current: Dict) -> Dict:
        """Analyze performance trends over time"""
        trends = {}

        # Get recent data (last 10 runs)
        recent = historical[-10:] + [{"metrics": current}]

        for metric in ["test_time", "lint_time", "security_time", "total_time"]:
            values = [
                run.get("metrics", {}).get(metric, 0)
                for run in recent
                if run.get("metrics", {}).get(metric, 0) > 0
            ]

            if len(values) >= 3:
                # Calculate trend
                avg_recent = statistics.mean(values[-3:])  # Last 3 runs
                avg_older = (
                    statistics.mean(values[:-3]) if len(values) > 3 else avg_recent
                )

                trend_percent = (
                    ((avg_recent - avg_older) / avg_older * 100) if avg_older > 0 else 0
                )

                trends[metric] = {
                    "current": current.get(metric, 0),
                    "recent_average": avg_recent,
                    "trend_percent": trend_percent,
                    "trend_direction": (
                        "increasing"
                        if trend_percent > 5
                        else "decreasing" if trend_percent < -5 else "stable"
                    ),
                }

        return trends

    def generate_report(self, analysis: Dict) -> str:
        """Generate human-readable performance report"""
        report = []
        report.append("=" * 60)
        report.append("🚀 CI/CD PERFORMANCE REPORT")
        report.append("=" * 60)
        report.append(f"Timestamp: {analysis['timestamp']}")
        report.append("")

        # Current metrics
        report.append("📊 CURRENT METRICS:")
        metrics = analysis["current_metrics"]
        for metric, value in metrics.items():
            if isinstance(value, float) and value > 0:
                report.append(f"  {metric}: {value:.1f}s")
            elif isinstance(value, bool):
                report.append(f"  {metric}: {'✅' if value else '❌'}")
            elif isinstance(value, int):
                report.append(f"  {metric}: {value}")
        report.append("")

        # Threshold analysis
        report.append("⚡ THRESHOLD ANALYSIS:")
        for metric, data in analysis["threshold_analysis"].items():
            status_emoji = {"OK": "✅", "WARNING": "⚠️", "FAILED": "❌"}
            emoji = status_emoji.get(data["status"], "❓")
            report.append(
                f"  {emoji} {metric}: {data['current']:.1f}s ({data['percentage']:.1f}% of {data['threshold']}s)"
            )
        report.append("")

        # Trend analysis
        if analysis["trend_analysis"]:
            report.append("📈 TREND ANALYSIS:")
            for metric, data in analysis["trend_analysis"].items():
                direction_emoji = {
                    "increasing": "📈",
                    "decreasing": "📉",
                    "stable": "➡️",
                }
                emoji = direction_emoji.get(data["trend_direction"], "❓")
                report.append(
                    f"  {emoji} {metric}: {data['trend_direction']} ({data['trend_percent']:+.1f}%)"
                )
            report.append("")

        # Alerts
        if analysis["alerts"]:
            report.append("🚨 ALERTS:")
            for alert in analysis["alerts"]:
                level_emoji = {"ERROR": "❌", "WARNING": "⚠️", "INFO": "ℹ️"}
                emoji = level_emoji.get(alert["level"], "❓")
                report.append(f"  {emoji} {alert['level']}: {alert['message']}")
        else:
            report.append("✅ NO ALERTS - Performance within acceptable ranges")

        report.append("")
        report.append("=" * 60)

        return "\n".join(report)

    def run_performance_check(self) -> bool:
        """Run complete performance check and return success status"""
        print("🚀 Starting performance monitoring...")

        # Run measurements
        current_metrics = self.run_timed_tests()

        # Analyze results
        analysis = self.analyze_performance(current_metrics)

        # Generate and display report
        report = self.generate_report(analysis)
        print(report)

        # Save metrics for trend analysis
        historical = self.load_metrics()
        historical.append(analysis)

        # Keep only last 50 runs to prevent file from growing too large
        if len(historical) > 50:
            historical = historical[-50:]

        self.save_metrics(historical)

        # Return success status (no ERROR level alerts)
        has_errors = any(alert["level"] == "ERROR" for alert in analysis["alerts"])
        return not has_errors


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Monitor CI/CD pipeline performance")
    parser.add_argument(
        "--metrics-file",
        default="performance_metrics.json",
        help="File to store performance metrics",
    )
    parser.add_argument(
        "--fail-on-regression",
        action="store_true",
        help="Exit with error code if performance regression detected",
    )

    args = parser.parse_args()

    tracker = PerformanceTracker(args.metrics_file)
    success = tracker.run_performance_check()

    if args.fail_on_regression and not success:
        print("\n❌ Performance regression detected!")
        sys.exit(1)

    print("\n✅ Performance monitoring completed successfully!")


if __name__ == "__main__":
    main()
