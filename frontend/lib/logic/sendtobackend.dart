import 'dart:convert';
import 'package:frontend/config.dart';
import 'package:http/http.dart' as http;

class Sendtobackend {

static Future<void> sendtoback(Map<String, dynamic> data) async {
	final dat = jsonEncode(data);

	final resp = await http.post(
	Uri.parse(config.getip()),
	headers: {'Content-Type': 'application/json'},	
	body: dat
	);
}

}
