import java.util.Arrays;

boolean lastThree(int value){
     return (value & 7) == 0;
}

void setup(){
  size(1200,600); 
  PImage img = createImage(1200, 600, RGB);
  
  PImage cat = loadImage("cat.png");
  PImage modified = loadImage("modifiedCat.png");
  
  cat.loadPixels(); 
  modified.loadPixels(); 
  
  int numPixels = 1200 * 600;
  
  for (int i = 0; i < numPixels ; i++) {
    color c = cat.pixels[i];
    color m = modified.pixels[i];
    
    int redc = (int)red(c);
    int greenc = (int)green(c);
    int bluec = (int)blue(c);
    
    int redm = (int)red(m);
    int greenm = (int)green(m);
    int bluem= (int)blue(m);

    if (redc != redm | greenc != greenm | bluec != bluem) {
      img.pixels[i] = color(#A020F0);
    }
    else {
      img.pixels[i] = color(#FFFFFF);
    }
    if( lastThree(redm) && lastThree(bluem)){
      img.pixels[i] = color(#00FF00); 
      if ((greenm & 3) == 0) {
        img.pixels[i] = color(#FF0000); // Red
      }
      else if ((greenm & 3) == 1) {
        img.pixels[i] = color(#0000FF); // Blue
      }
      else if ((greenm & 3) == 2) {
        img.pixels[i] = color(#FFFF00); // Yellow
      }
      else if ((greenm & 3) == 3) {
        img.pixels[i] = color(#00FF00); // Stays green
      }
    }
  }
  image(img, 0, 0);
}
