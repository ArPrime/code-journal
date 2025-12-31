# ex00_first_flutter_app
https://docs.flutter.dev/get-started/codelab

# Step by step

## 0
```dart
void main() {
  runApp(
    Container(
      color: Colors.yellow,
      child: Center(
        child: Text(
          'Hi, Flutter!',
          textDirection: TextDirection.ltr,
          style: TextStyle(fontSize: 32, color: Colors.blue),
        ),
      ),
    ),
  );
}
```

## 1
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: Container(
        color: Colors.yellow,
        child: Center(
          child: Text(
            'Hi, Flutter!',
            style:TextStyle(
              fontSize: 32,
              color: Colors.blue,
            ),
          ),
        ),
      ),
    )
  );
}
```

## 2 创建自己的 Widget 类
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp()); // 用【你自己创建的】Widget
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Container(
        color: Colors.yellow,
        child: Center(
          child: Text(
            '你好, Flutter!',
            style: TextStyle(
              fontSize: 32,
              color: Colors.blue,
            ),
          ),
        ),
      ),
    );
  }
}
```


# 3 把 home 页面也抽成独立的类
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),  // 改成用新的类
    );
  }
}

// 新增：首页组件
class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.yellow,
      child: Center(
        child: Text(
          '你好, Flutter!',
          style: TextStyle(
            fontSize: 32,
            color: Colors.blue,
          ),
        ),
      ),
    );
  }
}
```


# 4 用 Scaffold 替换 Container
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(        // Container 换成 Scaffold
      body: Center(         // child 换成 body
        child: Text(
          '你好, Flutter!',
          style: TextStyle(
            fontSize: 32,
            color: Colors.blue,
          ),
        ),
      ),
    );
  }
}
```