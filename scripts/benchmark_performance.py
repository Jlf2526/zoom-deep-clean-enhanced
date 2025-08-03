#!/usr/bin/env python3
"""
Performance Benchmark Script
Compare old vs new implementation performance

Created by: PHLthy215 (Enhanced by Amazon Q)
Version: 2.3.0 - Performance Benchmarking
"""

import sys
import os
import time
import asyncio
import logging
from typing import Dict, Any, List
from pathlib import Path

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

try:
    from zoom_deep_clean.performance_optimizations import PerformanceOptimizer
    from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced
    PERFORMANCE_MODULE_AVAILABLE = True
except ImportError as e:
    print(f"Performance module not available: {e}")
    PERFORMANCE_MODULE_AVAILABLE = False


class PerformanceBenchmark:
    """Benchmark performance improvements"""
    
    def __init__(self):
        self.setup_logging()
        self.results = {}
    
    def setup_logging(self):
        """Setup logging for benchmarks"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def benchmark_file_scanning(self) -> Dict[str, Any]:
        """Benchmark file scanning performance"""
        self.logger.info("🔍 Benchmarking file scanning performance...")
        
        # Test directories (smaller subset for benchmarking)
        test_directories = [
            "/Applications",
            "/Users/Shared",
            "/Library/Application Support"
        ]
        
        # Filter existing directories
        existing_dirs = [d for d in test_directories if os.path.exists(d)]
        
        if not existing_dirs:
            self.logger.warning("No test directories found for benchmarking")
            return {}
        
        results = {}
        
        # Benchmark old method (simulated sequential scanning)
        self.logger.info("📊 Testing sequential scanning...")
        start_time = time.time()
        sequential_files = self.simulate_sequential_scan(existing_dirs)
        sequential_time = time.time() - start_time
        
        results['sequential'] = {
            'time': sequential_time,
            'files_found': len(sequential_files),
            'directories_scanned': len(existing_dirs)
        }
        
        # Benchmark new method (parallel scanning)
        if PERFORMANCE_MODULE_AVAILABLE:
            self.logger.info("⚡ Testing parallel scanning...")
            start_time = time.time()
            parallel_files = asyncio.run(self.test_parallel_scan(existing_dirs))
            parallel_time = time.time() - start_time
            
            results['parallel'] = {
                'time': parallel_time,
                'files_found': len(parallel_files),
                'directories_scanned': len(existing_dirs)
            }
            
            # Calculate improvement
            if sequential_time > 0:
                improvement = ((sequential_time - parallel_time) / sequential_time) * 100
                results['improvement'] = {
                    'time_saved': sequential_time - parallel_time,
                    'percentage_improvement': improvement
                }
        
        return results
    
    def simulate_sequential_scan(self, directories: List[str]) -> List[str]:
        """Simulate the old sequential scanning method"""
        found_files = []
        
        for directory in directories:
            self.logger.info(f"Scanning {directory}...")
            
            # Simulate find command (simplified)
            for root, dirs, files in os.walk(directory):
                # Skip hidden directories and common exclusions
                dirs[:] = [d for d in dirs if not d.startswith('.') and 
                          d not in ['Caches', 'Trash', '__pycache__']]
                
                for file in files:
                    if 'zoom' in file.lower():
                        found_files.append(os.path.join(root, file))
                
                # Limit depth to avoid excessive scanning
                if root.count(os.sep) - directory.count(os.sep) > 3:
                    dirs.clear()
        
        return found_files
    
    async def test_parallel_scan(self, directories: List[str]) -> List[str]:
        """Test the new parallel scanning method"""
        optimizer = PerformanceOptimizer(self.logger, max_workers=4)
        
        def progress_callback(progress, message):
            self.logger.debug(f"Progress: {progress}% - {message}")
        
        return await optimizer.optimized_file_search(directories, progress_callback)
    
    def benchmark_process_management(self) -> Dict[str, Any]:
        """Benchmark process management performance"""
        self.logger.info("🛑 Benchmarking process management...")
        
        results = {}
        
        if PERFORMANCE_MODULE_AVAILABLE:
            optimizer = PerformanceOptimizer(self.logger)
            
            # Test process discovery
            start_time = time.time()
            processes = optimizer.process_manager.get_zoom_processes_batch()
            discovery_time = time.time() - start_time
            
            results['process_discovery'] = {
                'time': discovery_time,
                'processes_found': len(processes)
            }
            
            self.logger.info(f"Found {len(processes)} Zoom processes in {discovery_time:.3f}s")
        
        return results
    
    def benchmark_memory_usage(self) -> Dict[str, Any]:
        """Benchmark memory usage"""
        self.logger.info("💾 Benchmarking memory usage...")
        
        try:
            import psutil
            process = psutil.Process()
            
            # Initial memory
            initial_memory = process.memory_info().rss / 1024 / 1024  # MB
            
            # Create optimizer (simulates loading performance modules)
            if PERFORMANCE_MODULE_AVAILABLE:
                optimizer = PerformanceOptimizer(self.logger)
                
                # Memory after loading
                loaded_memory = process.memory_info().rss / 1024 / 1024  # MB
                
                return {
                    'initial_memory_mb': initial_memory,
                    'loaded_memory_mb': loaded_memory,
                    'memory_overhead_mb': loaded_memory - initial_memory
                }
            else:
                return {'initial_memory_mb': initial_memory}
        
        except ImportError:
            self.logger.warning("psutil not available for memory benchmarking")
            return {}
    
    def run_full_benchmark(self) -> Dict[str, Any]:
        """Run complete performance benchmark"""
        self.logger.info("🚀 Starting comprehensive performance benchmark...")
        
        benchmark_results = {
            'timestamp': time.time(),
            'system_info': self.get_system_info(),
            'file_scanning': {},
            'process_management': {},
            'memory_usage': {}
        }
        
        # File scanning benchmark
        try:
            benchmark_results['file_scanning'] = self.benchmark_file_scanning()
        except Exception as e:
            self.logger.error(f"File scanning benchmark failed: {e}")
        
        # Process management benchmark
        try:
            benchmark_results['process_management'] = self.benchmark_process_management()
        except Exception as e:
            self.logger.error(f"Process management benchmark failed: {e}")
        
        # Memory usage benchmark
        try:
            benchmark_results['memory_usage'] = self.benchmark_memory_usage()
        except Exception as e:
            self.logger.error(f"Memory usage benchmark failed: {e}")
        
        return benchmark_results
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get system information for benchmark context"""
        import platform
        
        info = {
            'platform': platform.system(),
            'platform_version': platform.release(),
            'architecture': platform.machine(),
            'python_version': platform.python_version(),
            'performance_module_available': PERFORMANCE_MODULE_AVAILABLE
        }
        
        try:
            import psutil
            info.update({
                'cpu_count': psutil.cpu_count(),
                'memory_total_gb': psutil.virtual_memory().total / 1024 / 1024 / 1024,
                'cpu_freq_mhz': psutil.cpu_freq().current if psutil.cpu_freq() else 'Unknown'
            })
        except ImportError:
            pass
        
        return info
    
    def print_results(self, results: Dict[str, Any]):
        """Print benchmark results in a readable format"""
        print("\n" + "="*60)
        print("🚀 PERFORMANCE BENCHMARK RESULTS")
        print("="*60)
        
        # System info
        if 'system_info' in results:
            print("\n📊 System Information:")
            for key, value in results['system_info'].items():
                print(f"  {key}: {value}")
        
        # File scanning results
        if 'file_scanning' in results and results['file_scanning']:
            print("\n🔍 File Scanning Performance:")
            fs_results = results['file_scanning']
            
            if 'sequential' in fs_results:
                seq = fs_results['sequential']
                print(f"  Sequential: {seq['time']:.2f}s ({seq['files_found']} files)")
            
            if 'parallel' in fs_results:
                par = fs_results['parallel']
                print(f"  Parallel:   {par['time']:.2f}s ({par['files_found']} files)")
            
            if 'improvement' in fs_results:
                imp = fs_results['improvement']
                print(f"  Improvement: {imp['percentage_improvement']:.1f}% faster")
                print(f"  Time saved:  {imp['time_saved']:.2f}s")
        
        # Process management results
        if 'process_management' in results and results['process_management']:
            print("\n🛑 Process Management Performance:")
            pm_results = results['process_management']
            
            if 'process_discovery' in pm_results:
                pd = pm_results['process_discovery']
                print(f"  Discovery: {pd['time']:.3f}s ({pd['processes_found']} processes)")
        
        # Memory usage results
        if 'memory_usage' in results and results['memory_usage']:
            print("\n💾 Memory Usage:")
            mem_results = results['memory_usage']
            
            if 'initial_memory_mb' in mem_results:
                print(f"  Initial:  {mem_results['initial_memory_mb']:.1f} MB")
            
            if 'loaded_memory_mb' in mem_results:
                print(f"  Loaded:   {mem_results['loaded_memory_mb']:.1f} MB")
            
            if 'memory_overhead_mb' in mem_results:
                print(f"  Overhead: {mem_results['memory_overhead_mb']:.1f} MB")
        
        print("\n" + "="*60)
    
    def save_results(self, results: Dict[str, Any], filename: str = None):
        """Save benchmark results to JSON file"""
        if filename is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"benchmark_results_{timestamp}.json"
        
        try:
            import json
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            self.logger.info(f"📄 Benchmark results saved to {filename}")
        except Exception as e:
            self.logger.error(f"Failed to save results: {e}")


def main():
    """Main benchmark execution"""
    print("🚀 Zoom Deep Clean Enhanced - Performance Benchmark")
    print("="*60)
    
    if not PERFORMANCE_MODULE_AVAILABLE:
        print("⚠️  Performance optimization module not available.")
        print("   Only basic benchmarking will be performed.")
        print()
    
    benchmark = PerformanceBenchmark()
    
    try:
        results = benchmark.run_full_benchmark()
        benchmark.print_results(results)
        benchmark.save_results(results)
        
        print("\n✅ Benchmark completed successfully!")
        
        # Provide recommendations
        if 'file_scanning' in results and 'improvement' in results['file_scanning']:
            improvement = results['file_scanning']['improvement']['percentage_improvement']
            if improvement > 50:
                print(f"🎯 Excellent performance improvement: {improvement:.1f}% faster!")
            elif improvement > 20:
                print(f"👍 Good performance improvement: {improvement:.1f}% faster")
            else:
                print(f"📈 Modest performance improvement: {improvement:.1f}% faster")
        
    except KeyboardInterrupt:
        print("\n🛑 Benchmark cancelled by user")
    except Exception as e:
        print(f"\n❌ Benchmark failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
