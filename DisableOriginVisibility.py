#
# Disable target object's Origin Visibility
#
def DisableOriginVisibility(objectList):
    subobjs = objectList.OutList
    for item in subobjs:
        try:
            item.Origin.Visibility = False
            DisableOriginVisibility(item)
        except:
                pass
        

