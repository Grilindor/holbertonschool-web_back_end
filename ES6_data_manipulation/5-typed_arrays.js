export default function createInt8TypedArray(length, position, value) {
  // Check if the position is within the valid range of the ArrayBuffer
  if (position >= length || position < 0) {
    // Throw an error if the position is outside the valid range
    throw new Error('Position outside range');
  }

  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create a DataView for the ArrayBuffer to manipulate its contents
  const dataView = new DataView(buffer);

  // Set the Int8 value at the specified position in the ArrayBuffer
  dataView.setInt8(position, value);

  // Return the DataView that contains the modified ArrayBuffer
  return dataView;
}
