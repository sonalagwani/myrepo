package com.example.userapi.service;

import com.example.userapi.model.User;
import com.example.userapi.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User saveUser(User user) {
        return userRepository.save(user);
    }

    public List<User> getUsersByNameAndCity(String name, String city) {
        if (name != null && city != null) {
            return userRepository.findByNameAndCity(name, city);
        } else if (name != null) {
            return userRepository.findByName(name);
        } else if (city != null) {
            return userRepository.findByCity(city);
        }
        return userRepository.findAll();
    }
}
