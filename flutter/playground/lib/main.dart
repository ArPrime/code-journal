import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: Container(
        color: Colors.yellow,
        child:Center(
          child: Text(
            '你好, Flutter!',
            style:TextStyle(
              fontSize: 32,
              color: Colors.blue,
            ),
          ),
        ),
      ),
    );
  }
}