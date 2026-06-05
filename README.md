Laboratory 6
GeoAI: Spatial Prediction Using Parcel-Based Feature Engineering 

--------
OVERVIEW
--------

---------------
EXPECTED OUTPUTS
----------------

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
Interpret: 
• where wrong predictions occur  
• whether errors cluster spatially  
• what spatial processes may explain errors  