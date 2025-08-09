import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header>
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <ul className="navbar-nav mx-3 mb-2 mb-lg-0 d-flex flex-row gap-4 w-100 justify-content-between">
          <div>
            <li className="nav-item no-select">
              <h1 className="text-xl">
                <Link
                  className="nav-link text-white text-decoration-none"
                  to="/"
                >
                  Invert Learn
                </Link>
              </h1>
            </li>
          </div>
          <div className="d-flex flex-row gap-4 justify-content-between">
            <li className="nav-item d-none d-lg-flex align-items-center">
              <Link
                className="nav-link  d-flex align-items-center"
                to="/signin"
              >
                Registrar usuario
              </Link>
            </li>
            <li className="nav-item d-none d-lg-flex align-items-center">
              <Link
                className="nav-link d-flex align-items-center"
                to="/user-list"
              >
                Lista de usuarios
              </Link>
            </li>
            <button
              className="navbar-toggler aspect-ratio-1x1"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="true"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
          </div>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
