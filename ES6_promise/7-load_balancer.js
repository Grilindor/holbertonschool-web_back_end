export default function loadBalancer(chinaDownload, USDownload) {
  // .race compare who promise is the fastest and return it
  return Promise.race([chinaDownload, USDownload]);
}
