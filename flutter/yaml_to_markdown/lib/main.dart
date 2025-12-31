import 'package:flutter/material.dart';
import 'yaml_converter.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'YAML to Markdown Converter',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const YamlToMarkdownConverter(),
    );
  }
}

class YamlToMarkdownConverter extends StatefulWidget {
  const YamlToMarkdownConverter({super.key});

  @override
  State<YamlToMarkdownConverter> createState() =>
      _YamlToMarkdownConverterState();
}

class _YamlToMarkdownConverterState extends State<YamlToMarkdownConverter> {
  final TextEditingController _yamlController = TextEditingController();
  final TextEditingController _markdownController = TextEditingController();

  void _convert() {
    setState(() {
      final yamlInput = _yamlController.text;
      final markdownOutput = convertYamlToMarkdown(yamlInput);
      _markdownController.text = markdownOutput;
    });
  }

  @override
  void dispose() {
    _yamlController.dispose();
    _markdownController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('YAML to Markdown Converter'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Left column - YAML input
            Expanded(
              flex: 1,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Expanded(
                    child: TextField(
                      controller: _yamlController,
                      maxLines: null,
                      expands: true,
                      decoration: const InputDecoration(
                        labelText: 'YAML Input',
                        border: OutlineInputBorder(),
                        alignLabelWithHint: true,
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: _convert,
                    style: ElevatedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 16),
                    ),
                    child: const Text(
                      'Convert to Markdown',
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 16),
            // Right column - Markdown output
            Expanded(
              flex: 1,
              child: TextField(
                controller: _markdownController,
                readOnly: true,
                maxLines: null,
                expands: true,
                decoration: const InputDecoration(
                  labelText: 'Markdown Output',
                  border: OutlineInputBorder(),
                  alignLabelWithHint: true,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
