use thiserror::Error;

#[derive(Debug, Error, Clone)]
#[error("{msg}")]
pub enum InvariantError {
    #[error("$df(x_n) == 0$")]
    DerivativeIsZero,
    #[error("{}", .0)]
    Generic(String),
}
