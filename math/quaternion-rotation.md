# Quaternion rotation
Status: draft

Quaternions are hypercomplex numbers with the form 

$$\mathbf{q} = q_0 + q_1\mathbf{i} + q_2\mathbf{j} + q_3\mathbf{k}$$

where $q_0$ is referred to as the *scalar* or *real* component and $q_1\mathbf{i} + q_2\mathbf{j} + q_3\mathbf{k}$ is the *vector* or *imaginary* component. Using quaternions for computing 3D rotations is best understood in the context of the [axis-angle representation](https://en.wikipedia.org/wiki/Axis–angle_representation) of 3D rotation. In the axis-angle formalism, rotations are specified by a unit vector $\mathbf{v} = v_x\mathbf{i} + v_y\mathbf{j} + v_z\mathbf{k}$ defining the axis of rotation and $\theta$ specifying the angle of rotation. 

<img src="axis-angle.png" width="350">

Given an axis-angle rotation, an equivalent *rotation quaternion* is
$$q_0 = \cos\left(\frac{\theta}{2}\right)$$
$$q_1 = v_x \sin\left(\frac{\theta}{2}\right)$$
$$q_2 = v_y \sin\left(\frac{\theta}{2}\right)$$
$$q_3 = v_z \sin\left(\frac{\theta}{2}\right)$$

A vector $\mathbf{v} \in R^3$ is rotated by $\mathbf{q}$ according to
$$
\begin{align*}
    \mathbf{v}' &= \mathbf{q}\mathbf{v}\mathbf{q}^*\\
    &= ({q_0}^2 - \left|\mathbf{q}\right|^2)\mathbf{v} + 2(\mathbf{q}\cdot\mathbf{v})\mathbf{q} + 2q_0(\mathbf{q}\times\mathbf{v})
\end{align*}  
$$

where 

$$\mathbf{v} = 0 + v_x\mathbf{i} + v_y\mathbf{j} + v_z\mathbf{k}$$ 
$$\left|\mathbf{q}\right| = \sqrt{{q_0}^2 + {q_1}^2 + {q_2}^2 + {q_3}^2}$$

$$\mathbf{q} \cdot \mathbf{v} = $$

$$\mathbf{q} \times \mathbf{v} = $$

$$\mathbf{q}_1\mathbf{q}_2 = (q_{1,0}q_{2,0} - )$$xs



https://danceswithcode.net/engineeringnotes/quaternions/quaternions.html