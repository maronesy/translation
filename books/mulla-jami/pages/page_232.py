# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 232 (printed ٢٣١)."""

PAGE_NUMBER = 232
PRINTED_PAGE = "٢٣١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "مثل: «زيدا اضربه، وزيدا لا تضربه».",
     "en": "…such as “Zayd—strike him” (Zaydan iḍribhu) and “Zayd—do not strike him” (Zaydan lā taḍribhu)."},
    {"type": "matn",
     "ar": "وإنما اختير في هذه المواضع أي: بعد حرف الاستفهام، والنفي، و«إذا» الشرطية، و«حيث»، وما قبل الأمر والنهي النصب في الاسم المذكور",
     "en": "The accusative is preferred in the noun mentioned in these places—that is, after the particle of interrogation and of negation, conditional “idhā” and “ḥaythu,” and before a command or prohibition—only"},
    {"type": "matn",
     "ar": "(إذ هي) أي: هذه المواضع (مواقع الفعل[[١]]) أي: مواضع وقوع الفعل فيها أكثر[[٢]]، فإذا نصب الاسم المذكور وقع فيها الفعل تقديرا، وإلا فلا.",
     "en": "(because they), that is, these places, (are positions of the verb), that is, places in which the verb occurs most often; so when the noun mentioned is put in the accusative, the verb occurs in them by supposition, and otherwise not."},
    {"type": "matn",
     "ar": "(و) كذلك يختار النصب في الاسم المذكور (عند خوف لبس المفسر[[٣]]) أي: التباس ما هو مفسر في حال النصب، لكن لا من حيث هو مفسر في هذه الحالة، بل من حيث هو خبر في حال الرفع (بالصفة)،",
     "en": "(And) likewise the accusative is preferred in the noun mentioned (when there is fear of confusing the explaining [verb]), that is, of confusing what is the explaining [verb] in the case of the accusative—not, however, as being an explainer in this state, but as being a khabar in the case of the nominative—(with a qualifier—bi-l-ṣifa);"},
    {"type": "matn",
     "ar": "فلا يعلم أنه خبر عن الاسم المذكور في حال الرفع مع موافقته للمعنى المقصود أو صفة له مع مخالفته للمعنى المقصود،",
     "en": "so it would not be known whether it is a khabar of the noun mentioned in the case of the nominative, agreeing with the intended meaning, or a qualifier of it, contradicting the intended meaning."},
    # REVIEW: print reads «عل تقدير» (for «على تقدير»); transcribed as printed.
    {"type": "matn",
     "ar": "فالالتباس إنما هو بين خبرية ذات ما هو مفسر عل تقدير النصب ووصفيته، لا بينه بوصف التفسير وبين الصفة؛ فإن التركيب لا يحتملهما معا",
     "en": "The confusion is thus only between the predicate-status of the very thing that is the explainer on the supposition of the accusative and its qualifier-status, not between it qua explainer and the qualifier; for the construction does not admit both together."},
    {"type": "matn",
     "ar": "(مثل) قوله تعالى: (﴿إنا كل شيء خلقناه بقدر﴾[[٤]]) بنصب «كل» على الإضمار بشريطة التفسير،",
     "en": "(Such as) His words, the Exalted: (“Indeed, We have created everything in measure”) (Qurʾān, Sūrat al-Qamar 54:49), with “kulla” in the accusative by suppression on condition of explanation."},
    {"type": "matn",
     "ar": "ولو رفع بالابتداء وجعل «خلقناه» خبرا له كان موافقا للنصب في أداء المقصود،",
     "en": "Had it been put in the nominative by inchoation, with “khalaqnāhu” made its khabar, it would agree with the accusative in conveying the intended meaning;"},
    {"type": "matn",
     "ar": "لكن خيف لبسه بالصفة، لاحتمال كون قوله: «بقدر» خبرا له وهو خلاف المقصود،",
     "en": "but its confusion with the qualifier was feared, since His words “bi-qadarin” might be its khabar, which is contrary to what is intended;"},
    {"type": "matn",
     "ar": "فإن الحكم على كل شيء بأنه مخلوق لنا بقدر، لا الحكم على كل شيء مخلوق لنا أنه بقدر،",
     "en": "for the judgment is about everything, that it is created by Us in measure—not the judgment about everything created by Us, that it is in measure;"},
    {"type": "matn",
     "ar": "فإنه يوهم كون بعض الأشياء الموجودة غير مخلوقة لله تعالى كما هو مذهب المعتزلة في الأفعال الاختيارية للعباد.",
     "en": "for that would suggest that some existing things are not created by Allah, the Exalted, as is the doctrine of the Muʿtazila concerning the voluntary acts of [His] servants."},
    {"type": "matn",
     "ar": "(ويستوي الأمران[[٥]]) أي: الرفع والنصب، فللمتكلم أن يختار كل واحد منهما بلا",
     "en": "(And the two are equal), that is, the nominative and the accusative, so the speaker may choose either of them without…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أنه لا يثبت المدعى لجواز تقدير فعل رافع، فيقال في «إذا زيد يقتله» إذا قتل زيد يقتله.",
     "en": "Against this: it does not establish the claim, since a verb governing the nominative may be supposed; so one says, for “idhā Zaydun yaqtuluhu,” “idhā qutila Zaydun yaqtuluhu.”"},
    {"type": "pair",
     "ar": "ويمكن أن يقال: الأولى مطابقة المفسر للمفسر، وفيه فوات ذلك.",
     "en": "It may be said: it is better for the explained to match the explainer, and in this that is lost."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن إضافة المواضع إلى الفعل باعتبار أن لها مزيد اختصاص بالفعل لا أنها مخصوصة به، يدل عليه اختيار النصب.",
     "en": "He means: the annexation of “places” to “the verb” is with respect to their having a greater affinity with the verb, not their being exclusive to it; the preference for the accusative indicates this."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "عطف على قوله: في الأمر.",
     "en": "Coordinated to his words “in the command.”"},
    {"type": "pair",
     "ar": "إنما أتى بلفظ الخوف للفرق بين تحقق اللبس وتوهمه، فإن الأول إنما يكون عند تساوى الاحتمالات، ورفعه واجب،",
     "en": "He used the word “fear” only to distinguish between confusion actually occurring and its being imagined: the first is only when the possibilities are equal, and removing it is obligatory;"},
    {"type": "pair",
     "ar": "والثاني عند رجحان البعض، ورفعه مختار كما نحن فيه.",
     "en": "the second is when some [possibility] is preponderant, and removing it is preferred, as in our case."},
    {"type": "pair",
     "ar": "وذلك لأن اللفظ إذا دار بين كونه خبرا وصفة كان الأولى أن يحمل على الخبر، لما فيه من الفائدة التامة.",
     "en": "That is because when a word oscillates between being a khabar and a qualifier, it is better to take it as the khabar, because of the complete information (fāʾida tāmma) it carries."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة القمر:٤٩.",
     "en": "Sūrat al-Qamar 54:49."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "في الاختيار.",
     "en": "In preference."},
]
