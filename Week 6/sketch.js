var song;


function setup() {
  createCanvas(500, 500);
  song = loadSound('bear/no.mp3');
}

function draw() {
  var t = second();
  // sec
  var Millis = millis();
  var s = millis()/1000;
  background(178,242,138);
  cursor('grab');
  strokeCap(ROUND);
  
  noStroke();
  fill(0,191,255,50);
  fill(0);
  rect(85,200,230,50);
  stroke(139,69,19);
  strokeWeight(8);
  
  //ear

  ellipse(70,150,100,100);
  ellipse(330,150,100,100);
  fill(165,121,19);
  ellipse(80,165,50,50);
  fill(165,121,19);
  ellipse(320,165,50,50);
  //face
  fill(0);
  ellipse(200,260,300,300);
  ellipse(200,340,170,140);

  //eye
  if (mouseIsPressed) {
    //song.play();
    close();
  
  } else {
    eye(mouseX,mouseY);
    //song.stop();
  }
 
  //highlight
  noStroke();
  fill(255,255,255);
  ellipse(95,150,20,20);
  ellipse(108,162,8,8);
  
}
   

    
function eye(x,y)
{
   
  if(x<=400)
    tx=x/400*15;
  else
    tx=15;
 if(y<=400)
   ty=y/400*30;
 else
  ty=30;
  noStroke();
  fill(255,248,244);
  fill(0,0,0,20);
  rect(105,205,50,20);
  rect(245,205,50,20);
  fill(165,121,19);
  rect(105+tx,205,30,45);
  rect(245+tx,205,30,45);
  stroke(139,69,19);
  line(105,205,155,205);
  line(105+tx,205,105+tx,250);
  line(135+tx,205,135+tx,250);
  arc(120+tx,250,30,30,0,PI);
  
  line(295,205,245,205);
  line(275+tx,205,275+tx,250);
  line(245+tx,205,245+tx,250);
  arc(260+tx,250,30,30,0,PI);
  
  noStroke();
  fill(255,255,255,50);
  fill(0,0,0,40);
  ellipse(120+tx,230+ty/2,20,20);
  ellipse(260+tx,230+ty/2,20,20);
  fill(255,255,255);
  ellipse(135+tx,215+ty,14,8);
  ellipse(275+tx,215+ty,14,8);
  stroke(139,69,19); 
  
  
  //mouth
  line(200,370,200,300);
  fill(165,121,19);
  ellipse(200,300,50,30);
  arc(200,380,70,14,PI,0);
  
}

function close()
{
  fill(165,121,19);
  line(200,330,200,300);
  fill(235,62,30);
  ellipse(200,300,50,30);
  line(115,220,165,240);
  line(115,260,165,240);
  line(285,220,235,240);
  line(235,240,285,260);
  noFill();
  strokeWeight(5);
  arc(200,340,40,14,PI,0);
  strokeWeight(8);
  song.play();
}

