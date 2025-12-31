import 'package:yaml/yaml.dart';

/// Converts YAML string to Markdown format.
///
/// Maps YAML hierarchy to Markdown headings and converts values to appropriate
/// Markdown syntax (lists, paragraphs, etc.).
String convertYamlToMarkdown(String yamlInput) {
  if (yamlInput.trim().isEmpty) {
    return '';
  }

  final dynamic yamlData = loadYaml(yamlInput);
  return _buildMarkdown(yamlData, 0);
}

/// Recursively builds Markdown from YAML data structure.
String _buildMarkdown(dynamic node, int depth) {
  final buffer = StringBuffer();

  if (node is YamlMap) {
    for (final entry in node.entries) {
      final key = entry.key.toString();
      final value = entry.value;

      // Add heading for the key
      buffer.writeln('${_getHeadingPrefix(depth)} $key');

      // Process the value
      if (value is YamlMap) {
        // Nested map - recurse with increased depth
        buffer.write(_buildMarkdown(value, depth + 1));
      } else if (value is YamlList) {
        // List - convert to Markdown bullets
        for (final item in value) {
          buffer.writeln('- $item');
        }
        buffer.writeln();
      } else if (value != null) {
        // Simple value - add as paragraph
        buffer.writeln(value.toString());
        buffer.writeln();
      } else {
        // Null value - just add blank line
        buffer.writeln();
      }
    }
  } else if (node is YamlList) {
    // Top-level list
    for (final item in node) {
      buffer.writeln('- $item');
    }
    buffer.writeln();
  }

  return buffer.toString();
}

/// Returns Markdown heading prefix based on depth.
/// depth 0 -> #, depth 1 -> ##, depth 2 -> ###, etc.
String _getHeadingPrefix(int depth) {
  return '#' * (depth + 1);
}
