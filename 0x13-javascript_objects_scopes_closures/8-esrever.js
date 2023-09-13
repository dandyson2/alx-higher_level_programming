#!/usr/bin/node
exports.esrever = (list) => {
  return list.reduceRight((array, current) => {
    array.push(current);
    return array;
  }, []);
};
