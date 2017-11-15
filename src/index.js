import {WebGLRenderer, PerspectiveCamera, BoxGeometry, MeshBasicMaterial, Mesh, Scene} from 'three';

window.load = function(){
  var scene = new Scene();
  var camera = new PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

  var renderer = new WebGLRenderer();
  renderer.setSize( window.innerWidth, window.innerHeight );
  console.log(renderer);
  
  console.log(document.getElementById("app"));
  
  document.getElementById("app").appendChild( renderer.domElement );

  var geometry = new BoxGeometry( 1, 1, 1 );
  var material = new MeshBasicMaterial( { color: 0x00ff00 } );
  var cube = new Mesh( geometry, material );
  
  scene.add( cube );

  camera.position.z = -10;
  
  renderer.render(scene, camera);

  // var render = function () {
  //   requestAnimationFrame( render );
    
  //   console.log('\o/');

  //   cube.rotation.x += 0.1;
  //   cube.rotation.y += 0.1;
    
  //   camera.position.z += 0.1
    
  // };

  // render();
}