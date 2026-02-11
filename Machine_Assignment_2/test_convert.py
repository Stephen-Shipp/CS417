#!/usr/bin/env python3
import sys
from convert import integer_to_base, fraction_to_base, decimal_to_base, convert, main, MAX_DIGITS


class TestSpecialCases:
    def test_zero(self):
        assert convert(0, 2) == "0"
        assert convert(0, 10) == "0"
        assert convert(0, 60) == "0"
    
    def test_one(self):
        assert convert(1, 2) == "1"
        assert convert(1, 10) == "1"
        assert convert(1, 60) == "1"


class TestIntegerConversion:
    def test_integer_to_base_2(self):
        assert integer_to_base(0, 2) == "0"
        assert integer_to_base(1, 2) == "1"
        assert integer_to_base(5, 2) == "1;0;1"
        assert integer_to_base(8, 2) == "1;0;0;0"
    
    def test_integer_to_base_10(self):
        assert integer_to_base(0, 10) == "0"
        assert integer_to_base(42, 10) == "4;2"
        assert integer_to_base(255, 10) == "2;5;5"
    
    def test_integer_to_base_16(self):
        assert integer_to_base(15, 16) == "15"
        assert integer_to_base(255, 16) == "15;15"
        assert integer_to_base(256, 16) == "1;0;0"


class TestBase2:
    def test_one_half(self):
        assert convert(0.5, 2) == "0.1"
    
    def test_one_quarter(self):
        assert convert(0.25, 2) == "0.0;1"
    
    def test_three_quarters(self):
        assert convert(0.75, 2) == "0.1;1"
    
    def test_one_eighth(self):
        assert convert(0.125, 2) == "0.0;0;1"
    
    def test_five_eighths(self):
        assert convert(0.625, 2) == "0.1;0;1"


class TestBase10:
    def test_one_half(self):
        assert convert(0.5, 10) == "0.5"
    
    def test_one_quarter(self):
        assert convert(0.25, 10) == "0.2;5"
    
    def test_one_tenth(self):
        assert convert(0.1, 10) == "0.1"


class TestBase60:
    def test_one_half(self):
        assert convert(0.5, 60) == "0.30"
    
    def test_one_quarter(self):
        assert convert(0.25, 60) == "0.15"
    
    def test_three_quarters(self):
        assert convert(0.75, 60) == "0.45"
    
    def test_one_sixth(self):
        assert convert(1/6, 60) == "0.10"


class TestNumbersGreaterThanOne:
    def test_whole_number_base_2(self):
        assert convert(5, 2) == "1;0;1"
        assert convert(8, 2) == "1;0;0;0"
    
    def test_mixed_number_base_2(self):
        assert convert(5.625, 2) == "1;0;1.1;0;1"
        assert convert(3.5, 2) == "1;1.1"
    
    def test_whole_number_base_10(self):
        assert convert(42, 10) == "4;2"
        assert convert(255, 10) == "2;5;5"
    
    def test_mixed_number_base_10(self):
        assert convert(42.5, 10) == "4;2.5"
    
    def test_whole_number_base_16(self):
        assert convert(255, 16) == "15;15"
        assert convert(256, 16) == "1;0;0"


class TestNegativeNumbers:
    def test_negative_fraction_base_2(self):
        assert convert(-0.5, 2) == "-0.1"
        assert convert(-0.75, 2) == "-0.1;1"
    
    def test_negative_whole_base_2(self):
        assert convert(-5, 2) == "-1;0;1"
    
    def test_negative_mixed_base_2(self):
        assert convert(-5.625, 2) == "-1;0;1.1;0;1"
    
    def test_negative_fraction_base_10(self):
        assert convert(-0.5, 10) == "-0.5"
    
    def test_negative_whole_base_10(self):
        assert convert(-42, 10) == "-4;2"


class TestRepeatingNumbers:
    def test_one_third_base_2(self):
        result = convert(1/3, 2)
        assert result.endswith("...")
    
    def test_one_fifth_base_2(self):
        result = convert(0.2, 2)
        assert result.endswith("...")
    
    def test_one_seventh_base_10(self):
        result = convert(1/7, 10)
        assert result.endswith("...")
    
    def test_negative_repeating(self):
        result = convert(-1/3, 2)
        assert result.startswith("-")
        assert result.endswith("...")


class TestAlgorithmDirectly:
    def test_fraction_uses_semicolon_separator(self):
        result = fraction_to_base(0.25, 2)
        assert ";" in result
    
    def test_fraction_stops_early_when_remainder_is_zero(self):
        result = fraction_to_base(0.5, 2)
        assert result == "1"
        assert "..." not in result
    
    def test_fraction_respects_max_digits(self):
        result = fraction_to_base(1/3, 2)
        # Remove "..." suffix, then count digits
        digits_part = result.replace("...", "")
        digit_count = len(digits_part.split(";"))
        assert digit_count == MAX_DIGITS


class TestMainFunction:
    def test_main_prints_header_with_base(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '16', '0.5'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "Base 10" in captured.out
        assert "Base 16" in captured.out
    
    def test_main_processes_base_2(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '2', '0.5', '0.25'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "0.5" in captured.out
        assert "0.1" in captured.out
        assert "0.25" in captured.out
        assert "0.0;1" in captured.out
    
    def test_main_processes_base_60(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '60', '0.5', '0.25'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "0.30" in captured.out
        assert "0.15" in captured.out
    
    def test_main_handles_zero(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '2', '0'])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        assert any("| 0" in line for line in lines[2:])
    
    def test_main_handles_numbers_greater_than_one(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '2', '5.625'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "5.625" in captured.out
        assert "1;0;1.1;0;1" in captured.out
    
    def test_main_handles_negative_numbers(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '2', '-0.75'])
        
        main()
        
        captured = capsys.readouterr()
        
        assert "-0.75" in captured.out
        assert "-0.1;1" in captured.out
    
    def test_main_columns_align(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, 'argv', ['convert.py', '2', '0.5', '0.123456789'])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # All lines should have the same length if columns are aligned
        line_lengths = [len(line) for line in lines]
        assert all(length == line_lengths[0] for length in line_lengths)