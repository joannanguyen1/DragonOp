const firebaseConfig = {
    apiKey: "AIzaSyCXe6K_5ao5Ew16wCxLNSzODnQGOgu5P-s",
    authDomain: "reportform-70e3f.firebaseapp.com",
    databaseURL: "https://reportform-70e3f-default-rtdb.firebaseio.com",
    projectId: "reportform-70e3f",
    storageBucket: "reportform-70e3f.appspot.com",
    messagingSenderId: "856593552545",
    appId: "1:856593552545:web:84a7a154c48f3be3f94ce0"
  };

  firebase.initializeApp(firebaseConfig);

  var reportFormDB = firebase.database().ref("reportForm");

  document.getElementById("reportForm").addEventListener("submit", submitForm);

  function submitForm(e){
    e.preventDefault();

    var yourName = getElementVal("yourName");
    var reportedPerson = getElementVal("reportedPerson");
    var reason = getElementVal("reason");

    saveMessages(yourName, reportedPerson, reason);
  }

  const saveMessages = (yourName, reportedPerson, reason) => {
    var newReportForm = reportFormDB.push();

    newReportForm.set({
      yourName : yourName,
      reportedPerson : reportedPerson,
      reason : reason,
    });
  };

  const getElementVal = (id) => {
    return document.getElementById(id).value
  };
