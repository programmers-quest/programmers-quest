#version 130

// Uniform inputs
uniform mat4 p3d_ModelViewProjectionMatrix;

// Vertex inputs
in vec4 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;

in vec2 frct_tilePosition;
in vec2 frct_tileCount;
in float frct_tileSheet;

// Output to fragment shader
out vec2 texcoord;
out vec2 tilePosition;
out vec2 tileCount;
out float tileSheet;

void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;

  texcoord = p3d_MultiTexCoord0;
  tilePosition = frct_tilePosition;
  tileCount = frct_tileCount;
  tileSheet = frct_tileSheet;
}
