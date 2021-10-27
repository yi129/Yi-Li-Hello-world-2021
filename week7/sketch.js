let video;
let poseNet;
let noseX = 0;
let noseY = 0;
let ear1X, ear1Y, ear2X, ear2Y;
let eye1X, eye1Y, eye2X, eye2Y;
let img;
let img2;

function setup() {
  createCanvas(640, 480);
  video = createCapture(VIDEO);
  video.hide();
  poseNet = ml5.poseNet(video, modelReady);
  poseNet.on('pose', gotPoses);
  img = loadImage('drop.png');
  img2 = loadImage('hat-png.png');
}

function gotPoses(poses) {
  // console.log(poses);
  if (poses.length > 0) {
    noseX = poses[0].pose.keypoints[0].position.x;
    noseY = poses[0].pose.keypoints[0].position.y;
    
    ear1X = poses[0].pose.keypoints[3].position.x;
    ear1Y = poses[0].pose.keypoints[3].position.y;
    
    ear2X = poses[0].pose.keypoints[4].position.x;
    ear2Y = poses[0].pose.keypoints[4].position.y;
        
        eye1X = poses[0].pose.keypoints[1].position.x;
    eye1Y = poses[0].pose.keypoints[1].position.y;
    
    eye2X = poses[0].pose.keypoints[2].position.x;
    eye2Y = poses[0].pose.keypoints[2].position.y;
  }
}

function modelReady() {
  console.log('model ready');
}

function draw() {
  image(video, 0, 0);
  //fill(255, 0, 0);
  //ellipse(noseX, noseY, 50);
  
  ear(ear1X, ear1Y*0.5);
  ear(ear2X, ear2Y*0.5);
    
    eye(eye1X, eye1Y, 80, 1);
  eye(eye2X, eye2Y, 80, -1);
  
  
}

function ear(x, y, size, n) {
    
    fill(52, 224, 197);
    noStroke();
    //ellipse(x, y+130, 100, 5);
    heart(x, y+180, 20,20);
    image(img, x-10,y+200,50,50);
    //image(img2, x-10,y+200,50,50);
  
  
    }

function eye(x, y, size, n) {
  

  let angle = frameCount * 2;

    
    fill(0);
    noStroke();
    //ellipse(x, y, size, size);
    heart(x, y, size,size);
    //ellipse(x+10, y, 100, 5)
  
    
    fill(52, 224, 197);
    noStroke();
    heart(x+cos(angle*2)*size/3, y+sin(angle)*size/3, size/1.5, size/2);
  //image(img, x-10, y-10);
    //image(img2, x-10,y-200,100,50);

}

function heart(x, y, size) {
  beginShape();
  vertex(x, y);
  bezierVertex(x - size / 2, y - size / 2, x - size, y + size / 3, x, y + size);
  bezierVertex(x + size, y + size / 3, x + size / 2, y - size / 2, x, y);
  endShape(CLOSE);
}