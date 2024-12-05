# scaps_scripts
This repo contains some SCAPS script files and bug fixes.

# Calculating the Filtered spectrum from the top cell of a tandem solar cell using SCAPS-1D
	Tandem Device construction
 ![image](https://github.com/naimur105/scaps_scripts/assets/58659352/cd5bbbf5-a3ab-4fc2-baf1-5aedc2860bdd)

Figure 1. Tandem solar cell design.

Save the device and give it a name. In this tutorial, it has the name: MASnI3_MAPbI3_tandem_revision.def
If you are following this tutorial, then simply download this def file and place inside the 'def' folder.
![image](https://github.com/user-attachments/assets/d10858a3-1efd-4b74-b174-8d9efae9e525)

Place the file called run_update_maxiter.bat and update_maxiter.py  in the SCAPS installation directory.
![image](https://github.com/naimur105/scaps_scripts/assets/58659352/5e8569c9-f75f-4ee0-9a1a-ab03cd964b8e)

Download the 'tandem from left adapt filters varying Rb.script' file and place inside the script folder.
![image](https://github.com/user-attachments/assets/86838e64-5282-45b9-a17d-c8cd2dfae8a7)

Now everything is set up for the simulaiton. Launch the SCAPS software and click Script set-up.
![image](https://github.com/user-attachments/assets/dad52fb4-8ebf-46f6-8ecb-1577df1612d3)
Press load:
![image](https://github.com/user-attachments/assets/98c280f4-af6e-4090-9ae1-3bdfc27d921c)
Load the script file (tandem from left adapt filters varying Rb.script) and click select.
![image](https://github.com/user-attachments/assets/2e6a1963-daed-4adf-ae76-16015f4793f5)
Press OK
![image](https://github.com/user-attachments/assets/69c7b5d2-e3b5-48ba-9358-493292684a01)
Now execute scirpt.
![image](https://github.com/user-attachments/assets/4f95d3ad-c16d-452e-a73c-9198448ac38b)
Wait for the simulation to complete.

# Finding the AM 1.5G spectrum and the filtered spectrum
After running the script, go to the SCAPS installation folder.
	Find the folder called “spectrum”. In that folder, find the file called AM1_5G 1 sun.spe . Open it with notepad, copy the columns and take the data in your desired plotting program (Excel, Origin etc.)
 
![image](https://github.com/naimur105/scaps_scripts/assets/58659352/36623537-96f0-4b7f-8f32-3b037fca2f62)

Find the folder called “filter”. In that folder, find a newly generated file called temporary bottom cell front transmission.ftr . Open it with notepad, copy the columns and take the data in your desired plotting program (Excel, Origin etc.). Place them beside the data from the AM1_5G columns. Only keep the column of the transmitted spectrum T(%). This will be the percentage of columns found for the specified top absorber thickness.
 
![image](https://github.com/naimur105/scaps_scripts/assets/58659352/3002de0a-c82e-4dfc-8aa1-3d7ecb7710c4)

3. Calculate with different absorber thickness again by editing the previously saved device (MASnI3_MAPbI3_tandem_revision.def in our case).
4. Repeat process 2 until you have the desired number of dataset.
5. Now we need to convert the T(%) to P(W/m2) for the filtered spectrum. In our case, we simply do Column B×(Column C)/100 and place it in Column C.
![image](https://github.com/naimur105/scaps_scripts/assets/58659352/716e94a4-fb92-4b3c-8747-f4d6d51eedaf)

7. The dataset is now complete. We can proceed to plotting.
 
![image](https://github.com/naimur105/scaps_scripts/assets/58659352/aa4be26e-bdf2-4961-b978-f62ff37774b0)

For your own device configuration, you need to slightly change the script. Refer to the Script chapter of the SCAPS manual to learn about the tandem device setup.


