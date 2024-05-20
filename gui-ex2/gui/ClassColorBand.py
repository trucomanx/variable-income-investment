import sys

class ColorBand():
    def __init__(self,band_list,color_list):
        self.band_list  = band_list;
        self.color_list = color_list;
        
        if isinstance(self.band_list, list)==False:
            sys.exit('The band_list should be a list');
        if isinstance(self.color_list, list)==False:
            sys.exit('The color_list should be a list');
        if all(isinstance(x, (int, float)) for x in self.band_list)==False:
            sys.exit('The band_list list must contain only numbers');
        if all(isinstance(x, str) for x in self.color_list)==False:
            sys.exit('The color_list list must contain only strings');
        if (len(self.band_list)+1)!=len(self.color_list):
            sys.exit('The color_list list should have plus one element than band_list');
        
        self.band_list=sorted(self.band_list);
    
    def color_of(self,value):
        
        color=self.color_list[0];
        
        for i,threshold in enumerate(self.band_list):
            if value>=threshold:
                color=self.color_list[i+1];
         
        return color;
