Laboratory 6
GeoAI: Spatial Prediction Using Parcel-Based Feature Engineering 

OVERVIEW
EXPECTED OUTPUTS
COMMIT MILESTONES:
A. Data Loading Reflection 
1. Why are parcels the prediction unit?
    Parcels are considered the most reliable unit of prediction in urban planning and GIS because they embody the very foundation of land management in which represents the legal, economic, and administrative identity of a piece of land. Parcels are also the basis for decisions about ownership, taxation, zoning, and development. Hence, planners and analysts can directly connect spatial data to real-world governance. Parcels serve as the bridge between spatial analysis and the lived realities of land use, ensuring that predictions and policies are grounded in the actual divisions that shape urban growth and community management.

2. What spatial processes might roads influence?
    Road networks serve as the fundamental framework for physical accessibility, transport efficiency, and human mobility. They shape spatial processes such as buffering, which generates polygons around roads at specified distances to delineate influence zones, noise corridors, or service areas. Road buffers can be overlaid with existing polygons to identify zoning areas or assess accessibility. Moreover, road lines can be used to subdivide larger polygons. This includes splitting administrative boundaries along highways to facilitate land parceling and the definition of planning units. Finally, polygons can be constructed around intersections using Voronoi or Thiessen methods, partitioning space based on proximity and thereby supporting equitable allocation of services and resources. 

3. Why might tourism affect parcel classification?
    Tourism affects how land parcels are classified because it alters both their function and perceived value. Parcels that were once residential, agricultural, or forested may be redefined as commercial or mixed-use when tourism facilities such as hotels, resorts, or restaurants emerge. This shift is driven not only by economic demand but also by the need to support visitor services and infrastructure. At the same time, hotspots or protected areas like coastal zones or heritage sites may be reclassified as protected parcels to manage tourism pressures. In addition, accessibility plays a role as well, since parcels near roads or transport hubs are frequently reassigned to accommodate tourism-related development. Large parcels may even be subdivided to create smaller units suitable for tourism enterprises, changing their classification in the process. Therefore, tourism introduces new spatial dynamics that require planners to reconsider parcel categories in order to balance development, conservation, and community needs.
4. Is machine learning occurring at this stage? 

B. Feature Engineering Reflection 
5. Why can geometry not be used directly in ML?  
6. Why are distances meaningful features?  
7. Which feature do you think is most influential? 

C. Model Reflection 
8. What does accuracy mean spatially?  
9. Can a model have high accuracy but poor spatial interpretation?  
10. What features may improve the model? 

D. Spatial Misclassification 
Interpret: 
• where wrong predictions occur  
• whether errors cluster spatially  
• what spatial processes may explain errors  