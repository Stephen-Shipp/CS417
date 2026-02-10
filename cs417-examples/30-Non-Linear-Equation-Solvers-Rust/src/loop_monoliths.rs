use super::errors::InvariantError;

const EPSILON: f64 = 10e-8;
const MAX_ITERATIONS: u64 = 100;
const ONE_HALF: f64 = 0.5;

/// Compute a solution to f using the bisection method
/// ```ignore
/// a0 = a
/// b0 = b
///
/// for n = 1, 2, ... do
/// xn = 0.5 (a_{n-1} + b_{n-1});
///     if f(xn) < 0 then
///         an = xn, bn = bn-1
///     end if;
///
///     if f(xn) > 0 then
///         an = an-1, bn = xn
///     end if;
///
///     if bn - an < eps then
///         break;
///     end if;
///
/// end for
///
pub fn bisection<F>(f: &F, a: f64, b: f64) -> Result<(u64, f64), InvariantError>
where
    F: Fn(f64) -> f64,
{
    let mut a_n = a;
    let mut b_n = b;

    let mut x_n = 0_f64;

    for n in 1..MAX_ITERATIONS {
        if f(b_n) < 0.0 {
            return Err(InvariantError::Generic(format!(
                "$f(b_{} = {}) < 0$",
                (n - 1),
                b_n
            )));
        }

        x_n = ONE_HALF * (a_n + b_n);

        let f_of_x_n = f(x_n);

        if f_of_x_n < 0.0 {
            a_n = x_n;
            // b_n = b_n-1 # unchanged
        }

        if f_of_x_n >= 0.0 {
            // a_n = a_n-1 # unchanged
            b_n = x_n;
        }

        // Stop Condition
        if (b_n - a_n).abs() < EPSILON {
            return Ok((n, x_n));
        }
    }

    Ok((MAX_ITERATIONS, x_n))
}

/// Compute a solution to f using the false position method
/// ```ignore
/// a0 = a
/// b0 = b;
///
/// for n = 1, 2, ... do
///     xn = an - ((an - bn)/(f(an) - f(bn)))f(an);
///
///     if f(xn) · f(an) > 0 then
///         an+1 = xn, bn+1 = bn
///     else
///         an+1 = an, bn+1 = xn
///     end if
/// end for
///
pub fn regula_falsi<F>(
    f: &F,
    a: f64,
    b: f64,
) -> Result<(u64, f64), InvariantError>
where
    F: Fn(f64) -> f64,
{
    let mut a_n = a;
    let mut b_n = b;

    let mut x_n = 0_f64;

    for n in 1..MAX_ITERATIONS {
        x_n = a_n - ((a_n - b_n) / (f(a_n) - f(b_n))) * f(a_n);

        if !x_n.is_finite() {
            return Err(InvariantError::Generic(
                "$f(a_n) - f(b_n) == 0$".to_owned(),
            ));
        }

        if f(x_n) * f(a_n) > 0.0 {
            a_n = x_n;
            // b_n - No change
        } else {
            // a_n - No Change
            b_n = x_n;
        }

        if (b_n - a_n).abs() < EPSILON {
            return Ok((n, x_n));
        }
    }

    Ok((MAX_ITERATIONS, x_n))
}

/// Compute a solution to f using the secant method
/// ```ignore
/// x_{n-1} = a0 = a
/// x_n = b0 = b;
///
/// for n = 1, 2, ... do
///     xn = xn - ((xn - x_n-1)/(f(xn) - f(x_n-1)))f(xn);
///
///     if f(xn) · f(an) > 0 then
///         an+1 = xn, bn+1 = bn
///     else
///         an+1 = an, bn+1 = xn
///     end if
/// end for
///
pub fn secant<F>(
    f: &F,
    x_n_minus_1_in: f64,
    x_n_in: f64,
) -> Result<(u64, f64), InvariantError>
where
    F: Fn(f64) -> f64,
{
    let mut x_n_minus_1 = x_n_minus_1_in;
    let mut x_n = x_n_in;

    for n in 2..MAX_ITERATIONS {
        let next_x_n =
            x_n - ((x_n - x_n_minus_1) / (f(x_n) - f(x_n_minus_1))) * f(x_n);

        if !next_x_n.is_finite() {
            return Err(InvariantError::Generic(
                "$f(x_n) - f(x_nm1) == 0$".to_owned(),
            ));
        }

        x_n_minus_1 = x_n;
        x_n = next_x_n;

        if (x_n - x_n_minus_1).abs() < EPSILON {
            return Ok((n, x_n));
        }
    }

    Ok((MAX_ITERATIONS, x_n))
}

/// Compute a solution to f using Newton's method.
/// ```ignore
/// Compute x_{n+1} = x_n - (f(x_n) / df(x_n)) until
/// |x_{n+1} - x_n| <= eps
///
pub fn newton<F1, F2>(
    f: &F1,
    df: &F2,
    x_0: f64,
) -> Result<(u64, f64), InvariantError>
where
    F1: Fn(f64) -> f64,
    F2: Fn(f64) -> f64,
{
    let mut x_n = x_0;

    for n in 1..MAX_ITERATIONS {
        let next_x_n = x_n - (f(x_n) / df(x_n));

        if !next_x_n.is_finite() {
            return Err(InvariantError::Generic("$df(x_n) == 0$".to_owned()));
        }

        if (x_n - next_x_n).abs() < EPSILON {
            return Ok((n, x_n));
        }

        x_n = next_x_n;
    }

    Ok((MAX_ITERATIONS, x_n))
}
