"""
Tests for CLI Enhanced module
Comprehensive testing of command-line interface functionality
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from io import StringIO

# Import the CLI module
from zoom_deep_clean.cli_enhanced import main


class TestCLIBasicFunctionality:
    """Test basic CLI functionality"""

    def test_help_argument(self):
        """Test --help argument displays help and exits"""
        with patch("sys.argv", ["cli_enhanced.py", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

    def test_version_argument(self):
        """Test --version argument displays version and exits"""
        with patch("sys.argv", ["cli_enhanced.py", "--version"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_dry_run_mode(self, mock_cleaner_class):
        """Test --dry-run argument execution"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        # Verify cleaner was called with dry_run=True
        call_args = mock_cleaner_class.call_args
        assert call_args[1]["dry_run"] is True
        mock_cleaner.run_deep_clean.assert_called_once()

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_verbose_mode(self, mock_cleaner_class):
        """Test --verbose argument execution"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--verbose", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        # Verify cleaner was called with verbose=True
        call_args = mock_cleaner_class.call_args
        assert call_args[1]["verbose"] is True

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_verbose_short_flag(self, mock_cleaner_class):
        """Test -v short form of verbose"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "-v", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["verbose"] is True

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_force_mode(self, mock_cleaner_class):
        """Test --force argument execution"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--force", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        mock_cleaner_class.assert_called_once()

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_force_short_flag(self, mock_cleaner_class):
        """Test -f short form of force"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "-f", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        mock_cleaner_class.assert_called_once()

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_no_backup_mode(self, mock_cleaner_class):
        """Test --no-backup argument execution"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--no-backup", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["enable_backup"] is False

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_vm_aware_mode(self, mock_cleaner_class):
        """Test --vm-aware argument execution"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--vm-aware", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["vm_aware"] is True

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_no_vm_mode(self, mock_cleaner_class):
        """Test --no-vm argument execution"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--no-vm", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["vm_aware"] is False

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_system_reboot_mode(self, mock_cleaner_class):
        """Test --system-reboot argument execution"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--system-reboot", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["system_reboot"] is True

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_custom_log_file(self, mock_cleaner_class):
        """Test --log-file argument with custom path"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        test_log = "/tmp/test.log"
        with patch(
            "sys.argv", ["cli_enhanced.py", "--log-file", test_log, "--dry-run"]
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["log_file"] == test_log

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_advanced_features_enabled(self, mock_cleaner_class):
        """Test --enable-advanced-features argument"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch(
            "sys.argv", ["cli_enhanced.py", "--enable-advanced-features", "--dry-run"]
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["enable_advanced_features"] is True

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_advanced_features_disabled(self, mock_cleaner_class):
        """Test --disable-advanced-features argument"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch(
            "sys.argv", ["cli_enhanced.py", "--disable-advanced-features", "--dry-run"]
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["enable_advanced_features"] is False

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_mac_spoofing_enabled(self, mock_cleaner_class):
        """Test --enable-mac-spoofing argument"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch(
            "sys.argv", ["cli_enhanced.py", "--enable-mac-spoofing", "--dry-run"]
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["enable_mac_spoofing"] is True

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_hostname_reset(self, mock_cleaner_class):
        """Test --reset-hostname argument"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--reset-hostname", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["reset_hostname"] is True

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_custom_hostname(self, mock_cleaner_class):
        """Test --new-hostname argument with custom hostname"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        test_hostname = "TestMac-Enhanced"
        with patch(
            "sys.argv",
            [
                "cli_enhanced.py",
                "--reset-hostname",
                "--new-hostname",
                test_hostname,
                "--dry-run",
            ],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["new_hostname"] == test_hostname

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_combined_arguments(self, mock_cleaner_class):
        """Test multiple arguments combined"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch(
            "sys.argv",
            ["cli_enhanced.py", "--dry-run", "--verbose", "--force", "--vm-aware"],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        call_args = mock_cleaner_class.call_args
        assert call_args[1]["dry_run"] is True
        assert call_args[1]["verbose"] is True
        assert call_args[1]["vm_aware"] is True


class TestCLIErrorHandling:
    """Test CLI error handling scenarios"""

    def test_invalid_arguments(self):
        """Test handling of invalid arguments"""
        with patch("sys.argv", ["cli_enhanced.py", "--invalid-argument"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code != 0

    def test_hostname_without_reset_flag(self):
        """Test --new-hostname without --reset-hostname fails"""
        with patch(
            "sys.argv", ["cli_enhanced.py", "--new-hostname", "TestMac", "--dry-run"]
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_cleaner_failure(self, mock_cleaner_class):
        """Test handling when cleaner fails"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = False
        mock_cleaner.was_cancelled_by_user.return_value = False
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_user_cancellation(self, mock_cleaner_class):
        """Test handling when user cancels operation"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = False
        mock_cleaner.was_cancelled_by_user.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.argv", ["cli_enhanced.py", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 130

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_security_error(self, mock_cleaner_class):
        """Test handling of security errors"""
        from zoom_deep_clean.cleaner_enhanced import SecurityError

        mock_cleaner_class.side_effect = SecurityError("Test security error")

        with patch("sys.argv", ["cli_enhanced.py", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 2

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_keyboard_interrupt(self, mock_cleaner_class):
        """Test handling of KeyboardInterrupt"""
        mock_cleaner_class.side_effect = KeyboardInterrupt()

        with patch("sys.argv", ["cli_enhanced.py", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 130

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_unexpected_exception(self, mock_cleaner_class):
        """Test handling of unexpected exceptions"""
        mock_cleaner_class.side_effect = Exception("Unexpected error")

        with patch("sys.argv", ["cli_enhanced.py", "--dry-run"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1


class TestCLIIntegration:
    """Test CLI integration with cleaner module"""

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_export_dry_run_success(self, mock_cleaner_class):
        """Test --export-dry-run functionality"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner.export_dry_run_operations.return_value = "/tmp/export.json"
        mock_cleaner_class.return_value = mock_cleaner

        with patch(
            "sys.argv",
            ["cli_enhanced.py", "--dry-run", "--export-dry-run", "/tmp/export.json"],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        mock_cleaner.export_dry_run_operations.assert_called_once_with(
            "/tmp/export.json"
        )

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_export_dry_run_without_dry_run_mode(self, mock_cleaner_class):
        """Test --export-dry-run without --dry-run shows warning"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch(
            "sys.argv",
            ["cli_enhanced.py", "--export-dry-run", "/tmp/export.json", "--force"],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0

        # Should not call export function
        mock_cleaner.export_dry_run_operations.assert_not_called()

    @patch("zoom_deep_clean.cli_enhanced.ZoomDeepCleanerEnhanced")
    def test_successful_completion_message(self, mock_cleaner_class):
        """Test successful completion shows correct message"""
        mock_cleaner = MagicMock()
        mock_cleaner.run_deep_clean.return_value = True
        mock_cleaner_class.return_value = mock_cleaner

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch("sys.argv", ["cli_enhanced.py", "--dry-run"]):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 0

        output = mock_stdout.getvalue()
        assert "Enhanced deep clean completed successfully" in output
