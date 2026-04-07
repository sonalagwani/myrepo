package com.example.userapi.controller;

import com.example.userapi.model.User;
import com.example.userapi.service.UserService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    /**
     * POST /api/users
     * Save a user with name and city.
     *
     * Request body example:
     * {
     *   "name": "John",
     *   "city": "New York"
     * }
     */
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        User savedUser = userService.saveUser(user);
        return new ResponseEntity<>(savedUser, HttpStatus.CREATED);
    }

    /**
     * GET /api/users?name=John&city=New York
     * Retrieve users by name and/or city.
     * Both parameters are optional — if both are provided, results are filtered by both.
     */
    @GetMapping
    public ResponseEntity<List<User>> getUsers(
            @RequestParam(required = false) String name,
            @RequestParam(required = false) String city) {
        List<User> users = userService.getUsersByNameAndCity(name, city);
        return ResponseEntity.ok(users);
    }
}
