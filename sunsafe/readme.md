

### UV Trends API
URL (render): https://sunsafe-web.onrender.com/api/uv-trends/
- Method: GET
- Description: Returns yearly UV index values for Melbourne.
- Example response:
 [
  {
    "year": 2016,
    "avg_uv_index": 14.97
  },
  {
    "year": 2017,
    "avg_uv_index": 13.6
  },
 ]

 ### CancerStatistics API
 URL (render)
 Full cancer data: https://sunsafe-web.onrender.com/api/cancer-stats/
 For entire Australia: https://sunsafe-web.onrender.com/api/uv-trends/?region=australia
 For Victoria: https://sunsafe-web.onrender.com/api/uv-trends/?region=victoria

 Description: Returns the Yearly cancer counts for Australia or Victoria specifically
 Example response:
 [
  {
    "year": 2016,
    "region": "Australia",
    "cancer_type": "Melanoma of the skin",
    "cases": 2200
  },
  {
    "year": 2016,
    "region": "Victoria",
    "cancer_type": "Melanoma of the skin",
    "cases": 2300
  },
  {
    "year": 2017,
    "region": "Australia",
    "cancer_type": "Melanoma of the skin",
    "cases": 2400
  }
]