import 'package:t1/t1.dart';
import 'package:test/test.dart';

void main() {
  test('calculate', () {
    expect(calculate(), 42);
  });
  test('calculate', () {
    expect(calculate2(4, 5), 2);
  });
  test('calasdfculate', () {
    expect(calculate2(4, 5), 20);
  });
}
