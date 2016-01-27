# vertex_model


The vertex model uses polygons, composed of vertices and edges, to illustrate the mechanics in formation of polygon sheets. This model has successfully been applied to fly wings and eyes in 2D. We are using this model to study the development of melanoma tumors and are extending the model to 3D. 

Simulations compute the energy and forces in the system using the following equations:

$U(R_{i}) = \sum_{\alpha} ka(A_{\alpha} - A_{0})^{2} + kp(P_{\alpha})

$F = - \frac{\partial U}{\partial R} $

where \\
$\alpha$ iterates overy every cell
$A_{0}$ is the preferred area
$P_{0}$ is the preferred perimeter
$k_{a}$ is the elasticity coefficient
$k_{p}$ is the surface tension coefficient



