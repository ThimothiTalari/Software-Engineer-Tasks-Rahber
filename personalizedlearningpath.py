class User:
    def __init__(self, user_id, interests=None, past_courses=None, performance_data=None):
        self.user_id = user_id
        self.interests = interests if interests else []
        self.past_courses = past_courses if past_courses else {}
        self.performance_data = performance_data if performance_data else {}

class Course:
    def __init__(self, course_id, title, prerequisites=None, difficulty=None, duration=None):
        self.course_id = course_id
        self.title = title
        self.prerequisites = prerequisites if prerequisites else []
        self.difficulty = difficulty
        self.duration = duration

class LearningPathGenerator:
    def __init__(self, users, courses):
        self.users = users
        self.courses = courses

    def generate_learning_path(self, user_id):
        user = self.users[user_id]
        interests = user.interests
        past_courses = user.past_courses
        performance_data = user.performance_data

        # Filter courses based on user interests
        filtered_courses = [course for course in self.courses if any(topic in course.title for topic in interests)]

        # Rank courses based on past engagement and performance data
        ranked_courses = self.rank_courses(filtered_courses, past_courses, performance_data)

        # Generate personalized learning path
        learning_path = self.generate_path(ranked_courses)

        return learning_path

    def rank_courses(self, courses, past_courses, performance_data):
        ranked_courses = []
        for course in courses:
            engagement_score = past_courses.get(course.course_id, 0)
            performance_score = performance_data.get(course.course_id, 0)
            total_score = engagement_score + performance_score
            ranked_courses.append((course, total_score))
        ranked_courses.sort(key=lambda x: x[1], reverse=True)
        return [course for course, _ in ranked_courses]

    def generate_path(self, courses):
        learning_path = []
        visited = set()

        def dfs(course):
            if course.course_id in visited:
                return
            visited.add(course.course_id)
            for prerequisite in course.prerequisites:
                dfs(prerequisite)
            learning_path.append(course)

        for course in courses:
            dfs(course)

        return learning_path

# Example usage:
user_data = {
    "user1": User("user1", interests=["Python", "Machine Learning"], past_courses={"course1": 5, "course2": 3}, performance_data={"course1": 90, "course2": 80}),
    # Add more user data as needed
}

course_data = [
    Course("course1", "Introduction to Python", prerequisites=[], difficulty="Beginner", duration=10),
    Course("course2", "Machine Learning Basics", prerequisites=[], difficulty="Intermediate", duration=15),
    Course("course3", "Advanced Python Programming", prerequisites=["course1"], difficulty="Advanced", duration=20),
    Course("course4", "Deep Learning Fundamentals", prerequisites=["course2"], difficulty="Advanced", duration=25),
    # Add more course data as needed
]

learning_path_generator = LearningPathGenerator(user_data, course_data)
learning_path = learning_path_generator.generate_learning_path("user1")
print("Learning Path for user1:")
for course in learning_path:
    print(course.title)
