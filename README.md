Data transformation process:

    +--------+    +---------+    +---------+
    | Order  |--->| Fetch   |--->| Parse   |--->
    +--------+    +---------+    +---------+    

    +--------+    +---------+    +---------+
    | Map    |--->| Norm    |--->| Export  |--->
    +--------+    +---------+    +---------+    

    +--------+    +---------+    +---------+
    | Read   |--->| Build   |--->| Render  |
    +--------+    +---------+    +---------+    

* 001 - Order - construct URLs, may need seed page
* 002 - Fetch - get the page with data
* 003 - Parse - extract data from the page

* 004 - Map   - extract meaningful data fields
* 005 - Norm  - normalize fields into common format
* 006 - Export - save in target format

* 007 - Read  - read open data set
* 008 - Build - process the data
* 009 - Render - make it beautiful
