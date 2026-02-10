use super::errors::InvariantError;

use std::rc::Rc;

#[derive(Clone)]
pub struct NewtonSolver<'a> {
    pub x_n: f64,
    f: Rc<dyn 'a + Fn(f64) -> f64>,
    df: Rc<dyn 'a + Fn(f64) -> f64>,
}

impl<'a> NewtonSolver<'a> {
    pub fn new(
        x_0: f64,
        math_f: &'a impl Fn(f64) -> f64,
        math_df: &'a impl Fn(f64) -> f64,
    ) -> Self {
        NewtonSolver {
            x_n: x_0,
            f: Rc::new(math_f),
            df: Rc::new(math_df),
        }
    }

    pub fn iter_mut(&mut self) -> &mut Self {
        self
    }

    fn next_state(&mut self) -> Result<Self, InvariantError> {
        let x_n = self.x_n;
        let f = &self.f;
        let df = &self.df;

        let next_x_n = x_n - (f(x_n) / df(x_n));

        if !next_x_n.is_finite() {
            return Err(InvariantError::DerivativeIsZero);
        }

        self.x_n = next_x_n;

        Ok(self.clone())
    }

    pub fn get_current_guess(&self) -> f64 {
        self.x_n
    }
}

impl<'a> std::iter::Iterator for NewtonSolver<'a> {
    type Item = NewtonSolver<'a>;

    fn next(&mut self) -> Option<Self::Item> {
        match self.next_state() {
            Err(_) => None,
            Ok(state) => {
                self.x_n = state.get_current_guess();

                Some(self.clone())
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    use hamcrest2::prelude::*;

    #[test]
    fn test_newton_solver_some() {
        let f = |x: f64| -> f64 { x.powf(2.0) };
        let df = |x: f64| -> f64 { 2.0 * x };

        let mut solver = NewtonSolver::new(-1.0, &f, &df);

        assert_eq!(solver.next(), Some(-1.0));
        assert_eq!(solver.next(), Some(-0.5));
        assert_eq!(solver.next(), Some(-0.25));
        assert_eq!(solver.next(), Some(-0.125));
        assert_eq!(solver.next(), Some(-0.0625));
    }

    #[test]
    fn test_newton_solver_none() {
        let f = |x: f64| -> f64 { x.powf(2.0) };
        let df = |x: f64| -> f64 { 2.0 * x };

        let mut solver = NewtonSolver::new(0.0, &f, &df);

        assert_eq!(solver.next(), Some(0.0));
        assert_eq!(solver.next(), None);
    }
}
