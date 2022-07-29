/******************************************************************************
 *  Deven Maheshwari & Daniela Maksin
 *  Period 3, Assignment 37
 *
 *  Compilation: javac Rational.java RationalClient.java
 *  Execution: java RationalClient
 *****************************************************************************/

public class Rational {
    //1
    private int x, y;

    //2
    public Rational() {
        this.x = 0;
        this.y = 1;
    }

    //3
    public Rational(int n) {
        this.x = n;
        this.y = 1;
    }

    //4
    public Rational(int n, int d) {
        if (d == 0) throw new RuntimeException("DIVISION BY ZERO");
        Boolean negative = (n > 0 && d < 0) || (n < 0 && d > 0);
        if (n == 0) {
            this.x = 0;
            this.y = 1;
        }
        else {
            if (negative) {
                this.x = Math.abs(n / gcd(n, d)) * -1;
            }
            else this.x = n / gcd(n, d);
            this.y = Math.abs(d / gcd(n, d));
        }
    }

    private int gcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    //5
    @Override
    public String toString() {
        return x + "/" + y;
    }

    //6
    public Rational plus(Rational rhs) {
        int help = lcm(getY(), rhs.getY());
        int help1 = (getX() * (help / getY()) + rhs.getX() * (help / rhs.getY()));
        return new Rational(help1, help);
    }

    private int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    //7
    public Rational minus(Rational rhs) {
        int help = lcm(getY(), rhs.getY());
        int help1 = (getX() * (help / getY()) - rhs.getX() * (help / rhs.getY()));
        return new Rational(help1, help);
    }

    //8
    public Rational times(Rational rhs) {
        int help1 = (getX() * rhs.getX());
        int help = (getY() * rhs.getY());
        return new Rational(help1, help);
    }

    //9
    public Rational dividesBy(Rational rhs) {
        int help1 = getX() / rhs.getY();
        int help = getY() * rhs.getX();
        return new Rational(help1, help);
    }

    //14
    public Rational invert() {
        return new Rational(getY(), getX());
    }

    public Rational negate() {
        return new Rational(-getX(), getY());
    }

    public Rational abs() {
        if (getX() >= 0 && getY() >= 0) return this;
        else return negate();
    }

    public double doubleValue() {
        if (getY() == 0) return 0.0;
        return (double) getX() / getY();
    }

    //16
    @Override
    public boolean equals(Object rhs) {
        if (rhs instanceof Rational) {
            Rational p = (Rational) rhs;
            return getX() == p.getX() && getY() == p.getY();
        }
        return false;
    }

}

