# Exercises

## Linear algebra

[Alx] Axler, *Linear Algebra Done Right* (3rd ed. 2015), Springer International Publishing, [Library link](https://csu-sb.primo.exlibrisgroup.com/permalink/01CALS_USB/122a7o7/alma991011070947602916).

1. (Alx, Exercise 1.B.1) Prove that $-(-v) = v$ for every $v \in V$. Here $V$ is a vector space. 

1. (Alx, Exercise 1.C.1) For each of the following subsets of $\mathbb{R}^3$, determine whether it is a sub-space of $\mathbb{R}^3$:

    1. {math}`\{ (x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1 + 2x_2 + 3x_3 = 0 \}`;
    1. {math}`\{ (x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1 + 2x_2 + 3x_3 = 4 \}`;
    1. {math}`\{ (x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1 x_2 x_3 = 0 \} `;
    1. {math}`\{ (x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1  = 5 x_3 \}`;
    
1. (Alx, Exercise 1.C.5) Is $\mathbb{R}^2$ a subspace of the complex vector space $\mathbb{C}^2$?

1. (Alx, Exercise 1.C.6)

    * Is {math}`\{ (a,b,c) \in \mathbb{R}^3 \mid a^3 = b^3 \}` a subspace of $\mathbb{R}^3$?
    * Is {math}`\{ (a,b,c) \in \mathbb{C}^3 \mid a^3 = b^3 \}` a subspace of $\mathbb{C}^3$?

1. (Alx, Exercise 1.C.12) Suppose $U_1$ and $U_2$ are subspaces of $V$. Prove that the intersection $U_1 \cap U_2$ is a subspace of $V$

    [Hint/Comment: Use the subspace criterion to show that an intersection is a subspace. 
    The same proof technique can be applied to show that (arbitrary) intersections of sub-groups, sub-rings, and ideals are groups, rings, and ideals, respectively. 
    We will see that an intersection of convex sets is convex.]

1. (Cf. Alx, Exercise 1.C.13) Suppose $U_1$ and $U_2$ are subspaces of $V$. Prove that the union $U_1 \cup U_2$ need not be a subspace of $V$. (It suffices to give a counter-example.)

1. (Cf. Alx, Exercise 2.A.1, 2.A.6) Suppose $v_1, v_2, v_3, v_4$ spans $V$. 
Prove that the list 
$$
v_1-v_2, v_2-v_3, v_3-v_4, v_4
$$ 
also spans $V$.
Also, in addition prove that if $v_1, v_2, v_3, v_4$ are linearly independent, then 
so are the list of vectors 
$$
v_1-v_2, v_2-v_3, v_3-v_4, v_4.
$$

1. (Cf. Alx, Exercise 2.A.3) Find a (real) number $t$ such that
$$ (3, 1, 4), (2, -3, 5), (5, 9, t)$$
is not linearly independent in $\mathbb{R}^3$.

1. (Cf. Alx, Exercise 2.B.2) 

    (a) Let $U$ be the subspace of $\mathbb{R}^5$ defined by
    ````{math}
    U = \{ ( x_1, x_2, x_3, x_4, x_5 ) \in \mathbb{R}^5 \mid x_1 = 3x_2 ~\text{and}~ x_3 = 7x_4 \}.
    ````
    Find a basis of $U$.

    (b) Extend the basis in part (a) to a basis of $\mathbb{R}^5$.

    (c) Find a subspace $W$ of $\mathbb{R}^5$ such that $\mathbb{R}^5 = U \oplus W$.

1. (Cf. Alx, Exercise 2.B.6) Suppose $v_1, v_2, v_3, v_4$ is a basis of $V$. 
Prove that
$$ 
v_1 + v_2, v_2 + v_3, v_3 + v_4, v_4
$$
is also a basis of $V$. 

    <!-- [Comment] Instead of proving this, you may outline your proof strategy.  -->

1. (Cf. Alx, Exercise 2.C.1) Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$ such that $\dim U = \dim V$. Prove that $U = V$.

    [Comment] Instead of proving this, you may outline your proof strategy. 

1. (Cf. Alx, Exercise 2.C.2) Show that the subspaces of $\mathbb{R}^2$ are precisely $\{0}\$, $\mathbb{R}^2$, and all lines in $\mathbb{R}^2$
through the origin.

1. (Cf. Alx, Exercise 2.C.12) Suppose $U$ and $W$ are both five-dimensional subspaces of $\mathbb{R}^9$. Prove that $U \cap W \neq \{ 0 \}$.

1. (Cf. Alx, Exercise 3.A.1) Suppose $b, c \in \mathbb{R}$. 
Define $T \colon \mathbb{R}^3 \to \mathbb{R}^2$ by
$$ 
T (x, y, z) = (2x - 4y + 3z + b, 6x + cxyz).
$$
Show that $T$ is linear if and only if $b = c = 0$.

1. (Cf. Alx, Exercise 3.A.4) Suppose $T$ is a linear transformation (linear map) from $V$ to $W$ and $v_1,v_2,v_3$ are vectors in $V$. 
Prove that $T(v_1), T(v_2), T(v_3)$ are linearly independent in $W$, 
then $v_1,v_2,v_3$ are linearly independent in $V$.

1. Let $V$ and $W$ be vector spaces and let $\mathscr{L}(V,W)$ denote the set of all linear maps from $V$ to $W$. 
Prove that $\mathscr{L}(V,W)$ is closed under addition and scalar multiplication. 

    [Comment:] Indeed, $\mathscr{L}(V,W)$ is a vector space. 

1. (The rank theorem) Suppose $V$ is a finite dimensional vector space and $T$ is a linear transformation from $V$ to a vector space $W$. Then 
$$
\dim V = \dim \operatorname{null} T + \operatorname{rank} T.
$$

1. Suppose $V = \mathbb{R}^1$. What is the dual basis of the basis $\{ 1 \}$ for $V$? What about for the basis of $\{ 2 \}$?

    [Remark:] The dual space is a set of linear maps from $V$ to $\mathbb{R}$. Thus, the dual basis consists of functions (linear maps). 

1. Suppose $V = \mathbb{R}^2$. What is the dual basis of the basis $\{ (1,0), (0,1) \}$ for $V$? What about for the basis $\{ (1,1), (1,2) \}$?

    [Remark:] Recall that these two sets are basis since the determinant of the matrix consisting of each of the two vectors are not zero. 

<!-- 1. (Cf. Alx, Exercise ..] -->

## Abstract algebra

All rings are commutative rings having 1.

1. Let $\mathbb{C}[x]$ be a polynomial ring over the complex number field. 
Prove that for any $c \in \mathbb{C}$, the map $\Phi \colon \mathbb{C}[x] \to \mathbb{C}$ which maps a polynomizl $f(x) \in \mathbb{C}[x]$ to $f(c)$ is a ring homomorphism. 
In addition, determine the kernel of this homomorphism.

> (First isomorphism theorem) Let $\Phi \colon R \to S$ be a ring homomorphism and $I$ the kernel of $\Phi$. 
> Then there exist ring homomorphisms $\psi \colon R \to R/I$ and $\phi \colon R/I \to S$ such that $\Phi = \phi \circ \psi$. 
> The homomorphism $\psi$ is surjective and $\rho$ is injective.

1. Recall that an ideal $P$ of a ring $R$ is prime if and only if $R/P$ is an integral domain. 
Use this fact to show that the kernel of the ring homomorphism in the previous exercise is a prime ideal.

1. Let $\mathbb{C}[x,y]$. Show that the ideals $(0), (x)$, and $(x,y)$ are prime ideals. 

    [Hint] To show that $(x,y)$ is a prime ideal, construct a ring homomorphism $\mathbb{C}[x,y] \to \mathbb{C}$ whose kernel is the ideal $(x,y)$.

1. Prove that an ideal $P$ of a ring $R$ is maximal if and only if $R/P$ is a field. 

1. What are the maximal ideals of $\mathbb{C}[x]$?

1. What are the maximal ideals of $\mathbb{C}[x,y]$?

## Calculus 

1. Find the equation of the tangent line of the curve $y = x^3 + 2x + 1$ at $x = 2$.

1. Find the equation of the tangent plane of the sphere $x^2 + y^2 + z^2 = 3$ at $(1,1,1)$.