import math
import sys
from finite_difference import main


class TestOutputStructure:
    def test_prints_header_row(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert "h" in lines[0]
        assert "x" in lines[0]
        assert "Approx. f'(x)" in lines[0]
        assert "Known f'(x)" in lines[0]
        assert "Abs. Error" in lines[0]

    def test_prints_separator_row(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert lines[1].startswith("|")
        assert ":" in lines[1]

    def test_prints_30_data_rows(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        # 1 header + 1 separator + 30 data rows = 32 lines
        data_rows = lines[2:]
        assert len(data_rows) == 30

    def test_columns_align(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        line_lengths = [len(line) for line in lines]
        assert all(length == line_lengths[0] for length in line_lengths)

    def test_all_lines_start_with_pipe(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        for line in lines:
            assert line.startswith("|")

    def test_all_lines_end_with_pipe(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        for line in lines:
            assert line.endswith("|")


class TestHValues:
    def test_first_row_h_label(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert "2^-01" in lines[2]

    def test_last_row_h_label(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert "2^-30" in lines[31]

    def test_all_h_labels_present(self, capsys):
        main()
        captured = capsys.readouterr()

        for n in range(1, 31):
            assert f"2^-{n:02d}" in captured.out


class TestXValue:
    def test_x_is_one_in_all_rows(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        for line in lines[2:]:
            assert "1.00000000" in line


class TestKnownDerivative:
    def test_known_value_is_cos_1(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        expected = f"{math.cos(1):.8f}"
        for line in lines[2:]:
            assert expected in line


class TestApproximation:
    def test_first_row_approx_value(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        h = 2.0 ** -1
        expected_approx = (math.sin(1 + h) - math.sin(1)) / h
        assert f"{expected_approx:.8f}" in lines[2]

    def test_approx_converges_toward_known(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        known = math.cos(1)
        # Extract approx values from data rows
        approx_values = []
        for line in lines[2:]:
            cols = [c.strip() for c in line.split("|") if c.strip()]
            approx_values.append(float(cols[2]))

        # Early errors should be larger than mid-range errors
        early_error = abs(approx_values[0] - known)
        mid_error = abs(approx_values[14] - known)
        assert early_error > mid_error

    def test_each_row_matches_formula(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        for i, line in enumerate(lines[2:], start=1):
            h = 2.0 ** (-i)
            expected_approx = (math.sin(1 + h) - math.sin(1)) / h
            assert f"{expected_approx:.8f}" in line


class TestAbsoluteError:
    def test_first_row_abs_error(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        h = 2.0 ** -1
        approx = (math.sin(1 + h) - math.sin(1)) / h
        expected_error = abs(math.cos(1) - approx)
        assert f"{expected_error:.8f}" in lines[2]

    def test_abs_error_is_nonnegative(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        for line in lines[2:]:
            cols = [c.strip() for c in line.split("|") if c.strip()]
            error = float(cols[4])
            assert error >= 0.0

    def test_abs_error_equals_difference(self, capsys):
        """Verify abs error = |known - approx| for each row."""
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        for line in lines[2:]:
            cols = [c.strip() for c in line.split("|") if c.strip()]
            approx = float(cols[2])
            known = float(cols[3])
            error = float(cols[4])

            expected_error = abs(known - approx)
            assert abs(error - expected_error) < 1e-7


class TestSampleOutput:
    """Verify output matches the sample values from the assignment."""

    def test_row_1_values(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert "0.31204800" in lines[2]
        assert "0.54030231" in lines[2]
        assert "0.22825430" in lines[2]

    def test_row_2_values(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert "0.43005454" in lines[3]
        assert "0.11024777" in lines[3]

    def test_row_3_values(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert "0.48637287" in lines[4]
        assert "0.05392943" in lines[4]

    def test_row_4_values(self, capsys):
        main()
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')

        assert "0.51366321" in lines[5]
        assert "0.02663910" in lines[5]