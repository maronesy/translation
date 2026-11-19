# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 205 (printed ٢٠٤)."""

PAGE_NUMBER = 205
PRINTED_PAGE = "٢٠٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "والقسم الثالث: وهو ما يكون مفردا، ولكن لا يكون معرفة مثل: (يا رجلا) مقولا (لغير معين) أي: لرجل غير معين.",
     "en": "The third category, what is single but not definite, as in: (“yā rajulan”—O a man) said (to one unspecified—li-ghayri muʿayyanin), that is, to an unspecified man."},
    {"type": "matn",
     "ar": "وهذا توقيت لنصب «رجلا»[[١]] لا تقييد له؛ لأنه إذا كان منصوبا لا يحتمل المعين[[٢]].",
     "en": "This is a specification of the occasion for the accusative of “rajulan,” not a restriction of it; because when it is in the accusative it cannot refer to a specified person."},
    {"type": "matn",
     "ar": "والقسم الرابع: وهو ما لا يكون مفردا ولا معرفة مثل: «يا حسنا وجهه ظريفا»[[٣]]،",
     "en": "The fourth category, what is neither single nor definite, as in “yā ḥasanan wajhuhu ẓarīfan” (O you whose face is fair, a graceful one)."},
    {"type": "matn",
     "ar": "ولم يورد المصنف لهذا القسم مثالا؛ إذ حيث اتضح انتفاء كل من القيدين بمثال سهل تصور انتفائهما معا،",
     "en": "The author did not give an example for this category, since, once the absence of each of the two conditions has been made clear by an example, it is easy to conceive of their being absent together;"},
    {"type": "matn",
     "ar": "فلا حاجة إلى إيراد مثال له على انفراده مع أن المثال الثاني يحتمله،",
     "en": "so there is no need to give an example of it on its own; besides which, the second example admits it."},
    {"type": "matn",
     "ar": "فيمكن أن يراد بقوله: «يا طالعا جبلا» هذه العبارة أعم من أن يراد بها معين أو غير معين.",
     "en": "So by his words “yā ṭāliʿan jabalan” this expression may be intended in a sense more general than its referring to a specified or an unspecified person."},
    {"type": "matn",
     "ar": "فأمثلة الأقسام بأسرها مذكورة، وهذه الأمثلة كلها مثال لما سوى المستغاث أيضا، فلا حاجة إلى إيراد مثال له على حدة.",
     "en": "Thus examples of all the categories are given; and all these examples are also examples of what is other than the mustaghāth, so there is no need to give a separate example for it."},

    # REVIEW: heading printed «توابع المنادي» (final yāʾ), as elsewhere in this print for المنادى; transcribed as printed.
    {"type": "section", "ar": "[توابع المنادي]",
     "en": "The Appositives (Tawābiʿ) of the Vocative Noun"},

    {"type": "matn",
     "ar": "(وتوابع المنادى[[٤]] المبني) على ما يرفع به[[٥]] (المفردة) حقيقة أو حكما،",
     "en": "(And the single appositives—tawābiʿ—of the indeclinable munādā), [indeclinable] on that by which it is put in the nominative, (being single—al-mufradatu), really or by status:"},
    {"type": "matn",
     "ar": "إنما قيد المنادى بكونه مبنيا؛ لأن توابع المنادى المعرب[[٦]] تابعة للفظه فقط[[٧]].",
     "en": "he restricted the munādā to its being indeclinable only because the appositives of the declinable munādā follow its form alone."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: يقال: يا رجلا بالنصب حال كون «رجل» لغير معين لا حال كون رجلا لغير معين.",
     "en": "That is: one says “yā rajulan” in the accusative when “rajul” is for an unspecified person; not [that] “rajulan” is [restricted] by its being for an unspecified person."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لأن رجلا حال كونه منصوبا لا يحتمل المعين، فلا حاجة إلى التقييد بغير المعين، فيكون مستدركا.",
     "en": "That is: because “rajulan,” while in the accusative, cannot refer to a specified person; so there is no need to restrict it to the unspecified, and [such a restriction] would be redundant."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال قدس سره في الحاشية: وإنما قيدناه بقوله: ظريفا ليكون نصا في كونه نكرة لم يقصد به معين،",
     "en": "He—may his secret be sanctified—said in the Ḥāshiya: “We restricted it by his saying ‘ẓarīfan’ only so that it is explicit in being an indefinite by which no specified person is intended;"},
    {"type": "pair",
     "ar": "فإنه لو قصد به معين، يقال: يا حسنا وجهه الظريف، انتهى.",
     "en": "for were a specified person intended by it, one would say: ‘yā ḥasanan wajhuhu al-ẓarīfu.’” End of quotation."},
    {"type": "pair",
     "ar": "اعلم أن شبه المضاف إذا قصد به معين وجب تعريف وصفه إلا إذا كان منعوتا بجملة أو ظرف، فإنه لا يوصف بالمعرفة،",
     "en": "Know that when a specified person is intended by what resembles the annexed, its qualifier must be definite, except when it is qualified by a sentence or an adverbial; for then it is not qualified by a definite noun."},
    {"type": "pair",
     "ar": "فلا يقال: يا حليما لا يعجل القدوس، بل يقال: قدوسا،",
     "en": "So one does not say “yā ḥalīman lā yaʿjalu al-quddūsu” (O Forbearing One who does not hasten, the Most Holy); rather one says “quddūsan.”"},
    {"type": "pair",
     "ar": "وذلك لأنه كره وصف الشيء بالمعرفة بعد وصفه بالنكرة وإن كان ذلك قبل النداء.",
     "en": "That is because qualifying a thing by a definite noun after qualifying it by an indefinite one was disliked, even if that was before the vocative."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يريد التوابع من كل وجه، أعني التابع في الصورة والحقيقة.",
     "en": "He means appositives in every respect, I mean what follows in form and in reality."},
    {"type": "pair",
     "ar": "فخرج يا أيها الرجل؛ لأنه تابع صورة منادى حقيقة.",
     "en": "So “yā ayyuhā al-rajulu” is excluded, because it is an appositive in form and a munādā in reality."},
    {"type": "pair",
     "ar": "وسيجيء في كلام الشارح نكتة عدم تقييد التابع هنا بما يخرجه،",
     "en": "The subtle reason for not restricting the appositive here by what would exclude it will come in the commentator’s words;"},
    {"type": "pair",
     "ar": "فمن ذكر هنا ما يجيء في كلام الشارح، فلم يتتبع كلامه أدنى تتبع.",
     "en": "so whoever mentions here what comes [later] in the commentator’s words has not followed his discourse even slightly."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: هو المتبادر من لفظ المبني هنا؛ لأنه قيل فيه: ويبنى دون غيره.",
     "en": "It has been said: this is what first comes to mind from the word “mabnī” here, because it is said of it “and it is made indeclinable,” and not of anything else."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "غير البدل والمعطوف الآتي حكمهما.",
     "en": "Other than the substitute (badal) and the coordinated noun (maʿṭūf), whose ruling is to come."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سواء كان منصوبا أو مجرورا نحو: يا لزيد وعمرو، ولم يحملوا على محله النصب، كما في \"أعجبني ضرب زيد وعمرا\".",
     "en": "Whether it is in the accusative or the genitive, as in “yā la-Zaydin wa-ʿAmrin”; they did not construe [the appositive] according to its place, the accusative, as in “Zayd’s beating, and ʿAmr’s, pleased me” (aʿjabanī ḍarbu Zaydin wa-ʿAmran)."},
]
