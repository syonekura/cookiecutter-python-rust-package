use pyo3::prelude::*;


#[pyfunction]
fn fibonacci_recursive_rust(n: u64) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        n=> fibonacci_recursive_rust(n-1) + fibonacci_recursive_rust(n-2)
    }
}

#[pyfunction]
fn fibonacci_iterative_rust(n: u64) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        n=> {
            let mut a= 0;
            let mut b = 1;
            let mut c = 0;

            for _ in 2..n {
                c = a + b;
                a = b;
                b = c;
            }
            c
        }
    }
}



/// A Python module implemented in Rust.
#[pymodule]
fn {{ cookiecutter.project_slug }}(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci_recursive_rust, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci_iterative_rust, m)?)?;
    Ok(())
}
