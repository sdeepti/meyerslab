### sRNA Phasing Analysis plugin for JBrowse
---

* Enable the following plugins within JBrowse within `tracks.conf`:
  * [Araport REST](https://github.com/Arabidopsis-Information-Portal/jbrowse/blob/stable/plugins/Araport/js/Store/SeqFeature/REST) with bindings to ADAMA
  * [CoGe MultiXYPlot](https://github.com/Arabidopsis-Information-Portal/jbrowse/blob/stable/plugins/CoGe/js/View/Track/Wiggle/MultiXYPlot.js)

```
[plugins]
Araport.location = ./plugins/Araport
CoGe.location = ./plugins/CoGe
```

* Ensure that the [srna_phasing_analysis_jbrowse](https://github.com/vivekkrish/meyerslab/tree/master/services/sRNA_phasing_analysis_jbrowse) adapter is registered and accessible via ADAMA

* Set up the following track configuration in JBrowse:
```
  "tracks": [
      {
          "label" : "sRNA_phasing_analysis_plus",
          "key" : "sRNA Phasing Analysis (+ strand)",
          "type" : "CoGe/View/Track/Wiggle/MultiXYPlot",
          "storeClass" : "Araport/Store/SeqFeature/REST",
          "baseUrl" : "https://api.araport.org/community/v0.3/vivek-dev/srna_phasing_analysis_jbrowse_v0.3",
          "autoscale" : "local",
          "query" : {
              "strand" : "+"
          },
          "coge": {
              "menuOptions" : [],
              "type" : "notebook",
              "experiments" : [
                  { "id" : "20", "name" : "<=20" },
                  { "id" : "21", "name" : "21" },
                  { "id" : "22", "name" : "22" },
                  { "id" : "23", "name" : "23" },
                  { "id" : "24", "name" : "24" },
                  { "id" : "25", "name" : ">=25" }
              ]
          }
      },
      {
          "label" : "sRNA_phasing_analysis_minus",
          "key" : "sRNA Phasing Analysis (- strand)",
          "type" : "CoGe/View/Track/Wiggle/MultiXYPlot",
          "storeClass" : "Araport/Store/SeqFeature/REST",
          "baseUrl" : "https://api.araport.org/community/v0.3/vivek-dev/srna_phasing_analysis_jbrowse_v0.3",
          "autoscale" : "local",
          "query" : {
              "strand" : "-"
          },
          "coge": {
              "menuOptions" : [],
              "type" : "notebook",
              "experiments" : [
                  { "id" : "20", "name" : "<=20" },
                  { "id" : "21", "name" : "21" },
                  { "id" : "22", "name" : "22" },
                  { "id" : "23", "name" : "23" },
                  { "id" : "24", "name" : "24" },
                  { "id" : "25", "name" : ">=25" }
              ]
          }
      }
   ],  
```

#### Contributors
[Vivek Krishnakumar](@vivekkrish) - JCVI
