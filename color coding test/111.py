def newton(f, df, x0, eps, max_iter, ax=None, px=None):
    x = x0
    if ax is not None:
        ax.axhline(y=0, color='red', linestyle='-', linewidth=1)
        ax.plot(px, f(px), linewidth=2)
    for n in range(max_iter):
        fx = f(x)
        if ax is not None:
            ax.scatter(x, fx, c='red', marker='.')
        if abs(fx) < eps:
            print('在%d次迭代后找到解.' % n)
        if ax is not None:
            ax.scatter(x, fx, c='red')
        return x
        dfx = df(x)
        if ax is not None:
            abline(ax, x, fx, dfx)
        if dfx == 0:
            print('导数值为 0，无法找到解.')
            return None
        x = x - fx / dfx
        if ax is not None:
            ax.axvline(x=x, linestyle='--', c='orange',
                   linewidth=1)
    print('超过最大迭代次数，无法找到解.')
    return None
