/**
 * capacitor.config.js
 *
 * Capacitor configuration for a Quasar mobile app.
 * This file is placed at the project root and read by the Capacitor CLI
 * when building native iOS/Android wrappers around the Quasar web app.
 *
 * Key settings:
 * - appId:  reverse-DNS identifier used by app stores (must be unique)
 * - appName: human-readable name shown under the app icon
 * - webDir:  folder Capacitor copies into the native project (Quasar build output)
 * - plugins: per-plugin configuration for Camera and Geolocation
 *
 * Permissions are declared in the native projects (Info.plist for iOS,
 * AndroidManifest.xml for Android) — the comments below document which
 * permission each plugin requires so the setup is not forgotten.
 */

const config = {
  // Unique reverse-DNS app identifier (e.g. com.company.appname)
  appId: 'com.example.quasarmobile',

  // Human-readable app name displayed on the home screen
  appName: 'Quasar Mobile App',

  // Directory containing the built web assets that Capacitor bundles
  // For Quasar this is the output of `quasar build -m capacitor`
  webDir: 'dist/capacitor',

  // Server configuration — keep webDir in sync with Quasar publicPath
  server: {
    androidScheme: 'https',
  },

  // Plugin-specific configuration
  plugins: {
    // ------------------------------------------------------------------
    // Camera plugin — captures photos from the device camera or gallery
    // https://capacitorjs.com/docs/apis/camera
    // ------------------------------------------------------------------
    Camera: {
      // Prompt the user to choose between camera and photo library
      source: 'PROMPT',
      // Save new photos to the gallery so they persist after capture
      saveToGallery: true,
      // Desired image quality (0-100)
      quality: 80,
      // Output format
      presentationStyle: 'fullscreen',
    },

    // ------------------------------------------------------------------
    // Geolocation plugin — retrieves the device GPS coordinates
    // https://capacitorjs.com/docs/apis/geolocation
    // ------------------------------------------------------------------
    Geolocation: {
      // Request high-accuracy GPS readings (may use more battery)
      enableHighAccuracy: true,
      // Timeout in milliseconds before giving up on a reading
      timeout: 10000,
    },
  },

  // ------------------------------------------------------------------
  // Permissions reference (declared in native config files, not here)
  // ------------------------------------------------------------------
  // iOS — add to ios/App/App/Info.plist:
  //   NSCameraUsageDescription       — "App needs camera access to take photos"
  //   NSPhotoLibraryUsageDescription — "App needs photo access to save images"
  //   NSPhotoLibraryAddUsageDescription — "App needs to save photos to your library"
  //   NSLocationWhenInUseUsageDescription — "App needs location to show your position"
  //
  // Android — add to android/app/src/main/AndroidManifest.xml:
  //   <uses-permission android:name="android.permission.CAMERA" />
  //   <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
  //   <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
  //   <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
  //   <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
};

// Capacitor expects a default export of the config object
export default config;
