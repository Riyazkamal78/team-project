# team-project

## How to run

Use Python 3 from the repository folder after the module pull requests are merged.

```sh
python login.py
python catalog.py
python cart.py
```

## Module branches

| Module | Branch | File |
| --- | --- | --- |
| Login | `feature-login` | `login.py` |
| Catalog | `feature-catalog` | `catalog.py` |
| Cart | `feature-cart` | `cart.py` |

## Team workflow

1. Start a feature branch from the latest `main`.
2. Commit the module changes and push the feature branch.
3. Open a pull request targeting `main`. Ask a teammate to review it.
4. Address review feedback and resolve merge conflicts on the feature branch.
5. Merge the pull request after approval.

## Merge conflict exercise

The catalog and cart branches both change the same module-list line below.
Merge the login and catalog pull requests first. Bring the updated `main` into
`feature-cart`, keep all three modules on the list, and push the resolution
to the open cart pull request.

Online Shopping Team Project for Software Engineering Experiment 15.

Modules: Login, Catalog, Cart
