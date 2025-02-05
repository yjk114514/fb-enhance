const headerJson = atob(headerBase64Url.replace(/-/g, '+').replace(/_/g, '/'));
const header = JSON.parse(headerJson);
console.log(header);