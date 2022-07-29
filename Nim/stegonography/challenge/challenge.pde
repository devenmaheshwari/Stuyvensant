import java.util.Arrays;

boolean lastThree(int value){
  return (value & 7) == 0;
}

void setup(){
  PImage space = loadImage("space.png");
  PImage modified = loadImage("modifiedSpace.png");
  
  size(1200,600);
  PImage img = createImage(space.width, space.height, RGB);
  
  space.loadPixels(); 
  modified.loadPixels(); 
  
  int numPixels = 1200 * 600;
  
  for (int i = 0; i < numPixels ; i++) {
    color c = space.pixels[i];
    color m = modified.pixels[i];
    
    int redc = (int)red(c);
    int greenc = (int)green(c);
    int bluec = (int)blue(c);
    
    int redm = (int)red(m);
    int greenm = (int)green(m);
    int bluem= (int)blue(m);

    if (redc != redm | greenc != greenm | bluec != bluem) {
      img.pixels[i] = color(#000000);
      if (!lastThree(bluem)){
        img.pixels[i] = color(#0000FF);
      }
    }
    else {
      img.pixels[i] = color(#FFFFFF);
    }

   }
   image(img, 0, 0);
}

// original --> blue channel ends in 000
// P3 32 32 -- -- - - - - -  - - -  (the string)
// display filename (after you get the string)
  
