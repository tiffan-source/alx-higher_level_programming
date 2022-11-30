#!/usr/bin/node

exports.converter = function (base) {
  return (number) => {
    return parseInt(number, 10).toString(base);
  };
};
