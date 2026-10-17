# concrete-durability-service-life-assessment.
assesment of durability of concrete based on service life assessment predictions
# Concrete Durability & Service Life Assessment Portfolio Project

## 1. Executive Summary
*   **Asset Type:** Marine Substructure Pier Cap
*   **Service Environment:** ACI Exposure Class C2 (Marine Tidal Zone)
*   **Reinforcement Details:** Grade 60 Carbon Steel at 50 mm clear concrete cover depth
*   **Primary Objective:** Determine the exact timeline of the Corrosion Initiation Phase ($t_i$) and evaluate material optimization frameworks to satisfy a mandatory 100-year design life under ACI CODE-365-24 metrics.

---

## 2. Forensic Field Diagnostics & Condition Survey
To evaluate existing conditions and establish calibration points for the transport models, a multi-tiered non-destructive evaluation (NDE) array was deployed:

*   **Electrochemical Corrosion Mapping (ASTM C876):** High-density half-cell potential grid mapping yielded readings ranging from -200mV to -450mV vs. a Copper-Copper Sulfate Electrode (CSE), demonstrating a localized >90% probability of active reinforcement corrosion.
*   **Carbonation Depth Profiling:** Visual indicators using a 1% phenolphthalein pH solution tracking across freshly fractured core samples mapped a maximum carbonation front depth of 35 mm over a 25-year service window.
*   **Surface Resistivity Tracking (AASHTO T 358):** Initial testing of the standard control mix indicated an average surface resistivity of 12 kΩ-cm, classifying the matrix within a moderate-to-high chloride ion permeability threshold.

---

## 3. Analytical Service Life Modeling
Using Fick's Second Law of Diffusion, the migration of chloride ions toward the reinforcing steel was calculated deterministically to evaluate the structural depassivation threshold ($C_{crit} = 1.2 \text{ kg/m}^3$):

$$\frac{\partial C}{\partial t} = D \cdot \frac{\partial^2 C}{\partial x^2}$$

### Analytical Evaluation Output (Fickian Error Function)
*   **Control Mix Performance:** The critical chloride threshold ($C_{crit}$) reaches the 50 mm rebar depth in exactly **34 years**, terminating the initiation phase ($t_i$) prematurely.
*   **Optimized Performance Mix:** Integrating 30% Slag Cement + 5% Silica Fume dramatically lowers the diffusion coefficient, extending the initiation phase ($t_i$) safely to **108 years**.

---

## 4. Life-Cycle Performance Comparison Matrix

| Parameter / Metric | Control Prescriptive Mix | High-Performance SCM Mix |
| :--- | :--- | :--- |
| **Binder Composition** | 100% Portland Cement Type I/II | 65% Portland + 30% Slag + 5% Silica Fume |
| **Diffusion Coeff. ($D$)** | $3.15 \times 10^{-8} \text{ mm}^2/\text{s}$ | $0.78 \times 10^{-8} \text{ mm}^2/\text{s}$ |
| **Time to Corrosion ($t_i$)** | **34 Years** | **108 Years** |
| **100-Year Structural Risk** | High (Requires active rehabilitation) | Negligible (Meets ACI 365 requirements) |

---

## 5. Engineering Conclusion & Mitigation
Relying on traditional prescriptive concrete dimensions fails to guarantee structural integrity in aggressive service environments. Transitioning to performance-based modeling frameworks under **ACI CODE-365-24** enables precision engineering of the cement paste microstructure. By replacing traditional binders with tailored SCM matrices and leveraging nonionic surfactant additives to alter clay mineral reactivity, civil infrastructure can successfully realize true multi-generational durability.
