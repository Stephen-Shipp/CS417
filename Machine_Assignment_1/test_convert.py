import sys
from convert import decimal_to_binary_fraction, convert, main, MAX_DIGITS


class TestSpecialCases:
    def test_zero(self):
        assert convert(0) == "0"
    
    def test_one(self):
        assert convert(1) == "1"


class TestTerminatingNumbers:
    def test_one_half(self):
        assert convert(0.5) == "0.1"
    
    def test_one_quarter(self):
        assert convert(0.25) == "0.01"
    
    def test_one_eighth(self):
        assert convert(0.125) == "0.001"
    
    def test_three_quarters(self):
        assert convert(0.75) == "0.11"
    
    def test_five_eighths(self):
        assert convert(0.625) == "0.101"


class TestRepeatingNumbers:
    def test_one_fifth(self):
        result = convert(0.2)
        assert result.endswith("...")
        assert len(result) == len("0.") + MAX_DIGITS + len("...")
    
    def test_one_tenth(self):
        result = convert(0.1)
        assert result.endswith("...")
    
    def test_one_third(self):
        result = convert(1/3)
        assert result.endswith("...")


class TestAlgorithmDirectly:
    def test_algorithm_produces_correct_digits_for_0625(self):
        # 0.625 * 2 = 1.25 -> digit 1, remainder 0.25
        # 0.25 * 2 = 0.5 -> digit 0, remainder 0.5
        # 0.5 * 2 = 1.0 -> digit 1, remainder 0
        assert decimal_to_binary_fraction(0.625) == "0.101"
    
    def test_algorithm_stops_early_when_remainder_is_zero(self):
        # 0.5 should terminate after just one digit
        result = decimal_to_binary_fraction(0.5)
        assert result == "0.1"
        assert "..." not in result


class TestMaxDigitsRespected:
    def test_repeating_number_caps_at_max_digits(self):
        result = decimal_to_binary_fraction(0.2)
        # Remove "0." prefix and "..." suffix to count digits
        digits_only = result[2:].replace("...", "")
        assert len(digits_only) == MAX_DIGITS


class TestMainFunction:
    def test_main_prints_header(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '0.5'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "Base 10" in captured.out
        assert "Base 2" in captured.out
        assert captured.out.startswith("|")
    
    def test_main_processes_single_argument(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '0.625'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "0.625" in captured.out
        assert "0.101" in captured.out
    
    def test_main_processes_multiple_arguments(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '0.5', '0.25', '0.2'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "0.5" in captured.out
        assert "0.25" in captured.out
        assert "0.2" in captured.out
        assert "0.1" in captured.out
        assert "0.01" in captured.out
        assert "0.00110011..." in captured.out
    
    def test_main_handles_zero(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '0'])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # Check that 0 appears in the data row
        assert any("| 0" in line for line in lines[2:])
    
    def test_main_handles_one(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '1'])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # Check that 1 appears in the data row
        assert any("| 1" in line for line in lines[2:])
    
    def test_main_columns_align(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '0.5', '0.123456789'])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # All lines should have the same length if columns are aligned
        line_lengths = [len(line) for line in lines]
        assert all(length == line_lengths[0] for length in line_lengths)