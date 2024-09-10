

## Explored Approaches for Data Quality Incident Detection

### 1. **Statistical Approach**: Analysis of Deals Contributing to *Unexplained PnL*

I initially started with a statistical approach aimed at identifying deals within portfolios affected by data quality (DQ) incidents. The main idea was to identify the deals with the highest contribution to unexplained PnL, considering them as more likely to be the source of data quality issues. However, when comparing the deals identified by this method with those mentioned in the incident reports, I found that the same deals were not consistently identified. After discussing with analysts, I concluded that this method was not adequate for addressing the problem.

### 2. **Machine Learning Approaches**

#### A. **Portfolio Classification**

I explored a classification approach at the portfolio level, aiming to categorize portfolios based on whether they were affected by a DQ incident or not. The main issue with this approach was that it did not take the temporal dimension into account. Our labels were based on incident reports without real-time versioning of modified data. Additionally, the continuity of the time series was partly broken, as some incidents were reported at the GOP (group of portfolios) level, introducing "gaps" in the available temporal data.

#### B. **Semi-Supervised Anomaly Detection at the Deal Level**

I then implemented a semi-supervised anomaly detection approach at the deal level. Using an Isolation Forest model with a custom scorer, this method integrated the analysts' expertise (who knew the expected proportions of incidents) and aimed to minimize false positives. Although this approach showed some effectiveness, it remains limited by the available data and imprecise labels.

### 3. **Other Explored and Abandoned Approaches**

I also considered several other methods that were ultimately not pursued due to data constraints:

- **Graph Neural Networks (GNNs)**: I considered using GNNs to model relationships between deals and portfolios, but this approach was abandoned as my data was not suitable for this graph structure: portfolios contain too many deals, and there are too many portfolios to construct a large number of graphs.
  
- **Portfolio Classification via Time Series**: A classification approach based on portfolio time series was explored, but had to be abandoned due to the "gaps" in my data, which prevented continuous chronological analysis.

- **PnL Reconstruction Using Available Features**: I attempted an approach to reconstruct PnL based on other available features in the data. However, this approach was abandoned, as my data was too far removed from the real data used by analysts to model the PnL.