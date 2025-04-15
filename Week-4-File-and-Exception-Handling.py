def process_file(input_filename, output_filename):
   
    try:
        with open(input_filename, "r") as file_in:
            content = file_in.read()  # Read content from the file
        
        # Convert all text to uppercase as a sample modification
        modified_content = content.upper()
        
        with open(output_filename, "w") as file_out:
            file_out.write(modified_content)  # Write the modified content
        
        print("Successfully processed the file. See", output_filename)
    except FileNotFoundError:
        print("Error: The file", input_filename, "not found.")
    except IOError:
        print("Error: Unable to read or write to one of the files.")

# Ask user for filenames
input_filename = input("Enter the input filename: ")
output_filename = input("Enter the output filename: ")

# Call the function 
process_file(input_filename, output_filename)
