Laboratory 6
GeoAI: Spatial Prediction Using Parcel-Based Feature Engineering 

--------
OVERVIEW
--------
This laboratory introduces GeoAI-based spatial prediction by integrating traditional GIS methods with machine learning. Parcel polygons serve as the prediction units, with spatial relationships transformed into numerical features for analysis. Using tools like GeoPandas, Scikit-learn, NumPy, Matplotlib, and QGIS, it allows to engineer spatial features, train a Random Forest model, and evaluate accuracy. The workflow demonstrates how geometry, accessibility, environment, and land-use context can be converted into explanatory variables for predictive analysis.

---------------
EXPECTED OUTPUTS
----------------
a. Engineered spatial features (area, perimeter, compactness, and distance-based variables).
b. A trained GeoAI classification model for parcel prediction.
c. Model evaluation using accuracy metrics.
d. Predicted parcel classifications stored in a GeoJSON file.
e. Visualization and interpretation of prediction results in QGIS.

------------------
COMMIT MILESTONES:
------------------
A. Data Loading Reflection 

1. Why are parcels the prediction unit?
    Parcels are considered the most reliable unit of prediction in urban planning and GIS because they embody the very foundation of land management in which represents the legal, economic, and administrative identity of a piece of land. Parcels are also the basis for decisions about ownership, taxation, zoning, and development. Hence, planners and analysts can directly connect spatial data to real-world governance. Parcels serve as the bridge between spatial analysis and the lived realities of land use, ensuring that predictions and policies are grounded in the actual divisions that shape urban growth and community management.

2. What spatial processes might roads influence?
    Road networks serve as the fundamental framework for physical accessibility, transport efficiency, and human mobility. They shape spatial processes such as buffering, which generates polygons around roads at specified distances to delineate influence zones, noise corridors, or service areas. Road buffers can be overlaid with existing polygons to identify zoning areas or assess accessibility. Moreover, road lines can be used to subdivide larger polygons. This includes splitting administrative boundaries along highways to facilitate land parceling and the definition of planning units. Finally, polygons can be constructed around intersections using Voronoi or Thiessen methods, partitioning space based on proximity and thereby supporting equitable allocation of services and resources. 

3. Why might tourism affect parcel classification?
    Tourism affects how land parcels are classified because it alters both their function and perceived value. Parcels that were once residential, agricultural, or forested may be redefined as commercial or mixed-use when tourism facilities such as hotels, resorts, or restaurants emerge. This shift is driven not only by economic demand but also by the need to support visitor services and infrastructure. At the same time, hotspots or protected areas like coastal zones or heritage sites may be reclassified as protected parcels to manage tourism pressures. In addition, accessibility plays a role as well, since parcels near roads or transport hubs are frequently reassigned to accommodate tourism-related development. Large parcels may even be subdivided to create smaller units suitable for tourism enterprises, changing their classification in the process. Therefore, tourism introduces new spatial dynamics that require planners to reconsider parcel categories in order to balance development, conservation, and community needs.

4. Is machine learning occurring at this stage?
      Machine learning does not take place during the data loading stage. At this point, the process is limited to importing datasets, verifying attribute integrity, and aligning coordinate systems. These steps are essential for ensuring that the spatial data is properly structured and consistent. This way, the foundation is established for subsequent analytical tasks. This stage is a preparatory phase that focuses on accuracy and compatibility rather than computation. Only after this stage will the datasets be applied to model training and prediction. 

B. Feature Engineering Reflection 

5. Why can geometry not be used directly in ML?
    Machine learning algorithms operate on numerical inputs rather than raw geometric objects such as polygons, lines, or points. To make spatial data usable, geometries must first be transformed into quantifiable features such as area, perimeter, compactness, or distance measures that can be quantifiable. These derived attributes allow the model to recognize and analyze patterns in a mathematical framework. In essence, the conversion of geometry into measurable indicators bridges the gap between spatial representation and computational analysis. This transformation ensures that complex spatial forms are reduced to values the algorithm can process. By doing so, machine learning can uncover relationships and trends that would otherwise remain hidden in raw geometric data. This step is critical for translating spatial complexity into actionable insights.

6. Why are distances meaningful features?
    Distances highlight how spatial relationships shape accessibility and land use. Parcels located closer to roads often enjoy greater benefits of connectivity which are near schools, tourist sites, or water networks may reflect distinct functional characteristics. These proximity-based influences provide important context for understanding how land is classified. By capturing such spatial dynamics, distance measures enable models to differentiate parcels more effectively. In reality, they serve as indicators of accessibility, opportunity, and constraint within the landscape. Distance is not just a measurement—it is a key factor that reveals how location drives land-use patterns.

7. Which feature do you think is most influential? 
    Land use is likely the most influential feature since surrounding land use often reflects how a parcel is utilized. At the same time, distance to roads is also critical, as accessibility strongly shapes residential, commercial, and industrial development patterns. Together, these factors provide powerful signals that help distinguish parcel classifications and explain how land use evolves across space.

C. Model Reflection 

8. What does accuracy mean spatially?
    Spatial accuracy measures how consistently the model predicts parcel classifications across geographic space. A higher accuracy indicates that the model is effectively capturing the relationship between parcel characteristics and their true classifications within the study area. In essence, it reflects the reliability of the model in translating spatial features into meaningful land-use outcomes.

9. Can a model have high accuracy but poor spatial interpretation? 
    Yes, a model may achieve high numerical accuracy yet still fail to capture the spatial processes underlying its predictions. It might correctly classify parcels but overlook geographic patterns, local variations, or clustering effects that are critical for spatial analysis. In such cases, accuracy alone can be misleading, as it does not guarantee that the model reflects the true spatial dynamics of the study area.

10. What features may improve the model?
    Additional spatial features that could strengthen the model include neighboring parcel density, the number of schools within a defined distance (e.g., 500 m), proximity to different road classes, tourism site density, land-use diversity around each parcel, distance to commercial centers, population density, and access to public transportation. These variables provide richer context about the parcel’s surrounding environment. By incorporating these, the model gains a deeper understanding of how accessibility, services, and land-use interactions shape development. This added detail can improve its ability to recognize meaningful spatial patterns and produce more accurate parcel classifications.

D. Spatial Misclassification

When evaluating parcel classification models, identifying exactly where errors occur highlights the limitations of geometric and proximity-based feature extraction. In this analysis, misclassifications regularly happen when agricultural parcels (Class A) are incorrectly predicted as residential zones (Class R). This error occurs because the physical attributes of these specific plots—such as small geometric areas, high shape compactness, and close proximity to newly developed roads or infrastructural facilities—heavily mimic the feature profiles of residential developments. When an agricultural parcel shares identical spatial geometries and distance metrics with a housing community, the data-driven model encounters feature overlap and struggles to isolate the true, legal class boundary (Qu et al., 2024; Ren et al., 2024).

Geographically, these classification errors do not manifest at random; instead, they exhibit distinct spatial clustering that follows Tobler’s First Law of Geography. Rather than being scattered uniformly across the map, the incorrect predictions pack tightly together within localized geographic pockets, particularly along urban-rural fringes and dynamic peri-urban transition zones (Leyk et al., 2018). These specific cluster zones represent hybrid spaces undergoing active structural transformations. Because neighboring parcels within these peripheral corridors share nearly identical physical surroundings, an error triggered by a misleading localized feature often cascades across adjacent parcels, producing dense clusters of misclassifications (Leyk et al., 2018).

Several real-world spatial processes explain why these clustering patterns form and confuse machine learning algorithms. Chief among these is urban sprawl, a dynamic trajectory where rural agricultural fields are gradually converted into residential landscapes, causing them to physically resemble urban environments before their official tax or legal descriptions are updated in administrative GIS registries. Furthermore, executing geometric operations like spatial joins can introduce "edge effects," causing parcels on zone boundaries to absorb conflicting contextual values from adjacent neighborhoods. Ultimately, because the Random Forest model relies entirely on visible physical measurements, it remains blind to underlying non-spatial constraints such as municipal zoning policies, socio-economic factors, and historical land protections—that legally govern how a piece of land must be utilized (Qu et al., 2024; Ren et al., 2024).

E. 

References:
Leyk, S., Uhl, J. H., Balk, D., & Jones, B. (2018). Assessing the accuracy of multi-temporal built-up land layers across rural-urban trajectories in the United States. Remote Sensing of Environment, 204, 898–917. https://doi.org/10.1016/j.rse.2017.08.035

Qu, S., Wang, H., Hu, Z., Wang, Z., & Hu, S. (2024). Mixed-use urban land parcels identification integrating geospatial data and machine learning. Geo-spatial Information Science, 1–14. https://doi.org/10.1080/10095020.2024.2374996

Ren, Y., Xie, Z., & Zhai, S. (2024). Urban land use classification model fusing multimodal deep features. ISPRS International Journal of Geo-Information, 13(11), 378. https://doi.org/10.3390/ijgi13110378
