# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 134 (printed ١٣٣)."""

PAGE_NUMBER = 134
PRINTED_PAGE = "١٣٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "ومستندهما في ذلك قول الشاعر:",
     "en": "Their basis for that is the saying of the poet:"},
    {"type": "verse",
     "ar": "جزى ربه عني عدي بن حاتم[[١]]        جزاء الكلاب العاويات وقد فعل",
     "en": "“May his Lord requite ʿAdī ibn Ḥātim on my behalf with the requital of howling dogs — and indeed He has done so.”"},
    {"type": "matn",
     "ar": "وأجيب عنه: بأن هذا لضرورة الشعر، والمراد عدم جوازه في سعة الكلام، وبأنه لا نسلم أن الضمير يرجع إلى «عدي»، بل إلى المصدر[[٢]] الذي يدل عليه الفعل، أي: «جزى رب الجزاء».",
     "en": "The reply to it is: that this is on account of poetic licence, and what is meant [by impermissibility] is that it is not permitted in the free scope of [ordinary] speech; and that we do not concede that the pronoun refers back to “ʿAdī,” but rather to the verbal noun (maṣdar) which the verb indicates — that is: “the Lord of requital requited.”"},

    # ---------------- Section heading ----------------
    {"type": "section",
     "ar": "[تقديم الفاعل على المفعول]",
     "en": "The Priority of the Agent over the Object"},

    {"type": "matn",
     "ar": "(وإذا انتفى الإعراب) الدال على فاعلية الفاعل، ومفعولية المفعول بالوضع (لفظا[[٣]] فيهما) أي: في الفاعل المتقدم ذكره صريحا وفي ضمن الأمثلة[[٤]] أيضا، والمفعول المتقدم ذكره في ضمن الأمثلة[[٥]] (والقرينة) أي: الأمر الدال عليهما لا بالوضع[[٦]]؛ إذ",
     "en": "(And when the inflection is absent) — [the inflection] that indicates by convention the agenthood of the agent and the objecthood of the object — (verbally in both of them), that is: in the agent whose mention has already come, explicitly and also within the [foregoing] examples, and in the object whose mention has come within the examples — (then the contextual indicator [al-qarīna]), that is: the thing that indicates the two of them not by convention; for"},

    {"type": "rule"},

    # ---------------- Footnote 5 (continued from previous page) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "إليه بلا قرينة غير جائز، وقد يقال: إن إعمال الثاني يقتضي إلغاء الأول في الاسم الظاهر، فلو أظهر لم يظهر كونه ملغى.",
     "en": "[the deletion of the term of annexation (al-muḍāf ilayhi)] without an indicator is impermissible; and it may be said: employing the second [governor] entails cancelling the first with respect to the overt noun, so were [the noun] to be made overt, its being cancelled would not appear."},
    {"type": "pair",
     "ar": "قال العصام: قوله: «وذلك غير جائز خلافا للأخفش وابن جني» لا مطلقا، بل إذا اتصل بالفاعل ضمير المفعول به أو بالمفعول به ضمير الفاعل،",
     "en": "Al-ʿIṣām said: His words, “and that is impermissible, contrary to al-Akhfash and Ibn Jinnī,” [hold] not absolutely, but [only] when the pronoun of the object is attached to the agent, or the pronoun of the agent to the object;"},
    {"type": "pair",
     "ar": "بل لم يخالفا في عدم جواز الإضمار قبل الذكر لفظا ورتبة وإن اشتهر ذلك منهما، بل اتفقا فيه وخالفا في لزومه في المثال المذكور كما أوضحناه لك.",
     "en": "indeed, the two of them did not dissent regarding the impermissibility of pronominalization before the [explicit] mention both verbally and in rank — even though that [dissent] is famously ascribed to them — rather they agreed upon it and dissented [only] over its being entailed in the said example, as we have made clear to you."},
    {"type": "pair",
     "ar": "ففي قوله: «خلافا للأخفش وابن جني» نظر. ولك أن تقول الخلاف في تأخر مرجع الضمير لفظا ورتبة، لا في قوله: «وذلك غير جائز».",
     "en": "So in his saying “contrary to al-Akhfash and Ibn Jinnī” there is [ground for] reconsideration. You may [also] say that the disagreement concerns the antecedent of the pronoun coming later both verbally and in rank, not his statement “and that is impermissible.”"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الجملة دعائية. والمراد بالكلاب العاويات: إما شرار الناس أو حقيقتها.",
     "en": "The sentence is a supplication. What is meant by “the howling dogs” is either the worst of people or [dogs in] their literal sense."},
    {"type": "pair",
     "ar": "قال قدس سره في الحاشية: عوى الكلب يعوي عواء إذا صاح، انتهى. وقد فعل جملة إخبارية وقعت على سبيل التفاؤل بأن الدعاء قد أجيب.",
     "en": "He, may his secret be sanctified, said in the gloss: “ʿawā al-kalbu yaʿwī ʿuwāʾan” [means] when [the dog] barks. End [of quotation]. And “qad faʿala” (“and indeed He has done [so]”) is a declarative sentence occurring by way of an auspicious presage that the supplication has been answered."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جعل الضمير إلى «عدي» هو المعنى الجزيل الذي لا يكاد يتخطاه البليغ؛ لأنه الموافق للعرف من حوالة الرجل المسيء إلى ربه، ولأن الرب هو الملجأ للرجل، فإذا انتقم للمظلوم منه يكون أشد عليه.",
     "en": "Making the pronoun refer to “ʿAdī” is the rich meaning that the eloquent one can scarcely bypass; because it accords with custom, [namely] referring the offending man [’s recompense] to his Lord, and because the Lord is the refuge of the man, so that when He takes retribution from him on behalf of the wronged, it is the harsher upon him."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "تمييز، أي: إذا انتفى لفظ الإعراب.",
     "en": "[It is] a specification (tamyīz); that is: when the [overt] wording of the inflection is absent."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فإن إحضار الفرد متضمن لإحضار جنسه خصوصا إذا لم يكن الغرض متعلقا بخصوص فرد كما في التمثيلات.",
     "en": "For bringing to mind the individual comprises bringing to mind its genus, especially when the aim is not tied to a particular individual, as is the case in [these] illustrative examples."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أو في ضمن ذكر المقابل الذي هو الفاعل لانتقال الذهن من أحد المتقابلين إلى الآخر.",
     "en": "Or [it comes] within the mention of the counterpart, which is the agent, on account of the mind’s passing from one of two correlatives to the other."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أنه إن أريد لا بالوضع له يلزم أن يكون اللفظ الدال على المعنى المجازي قرينة عليه، ولم يقل به أحد.",
     "en": "Against this [it may be said]: if what is meant is “not by [its] being coined for it,” then it follows that the wording indicating the figurative meaning would be an indicator (qarīna) for it, and no one has held this."},
    {"type": "pair",
     "ar": "وإن أريد لا بالوضع له ولا لما يستلزمه يلزم ألا يكون اللفظ قرينة بمعناه التضمني والالتزامي مع أنه قد يكون اللفظ قرينة لهما.",
     "en": "And if what is meant is “neither by [its] being coined for it nor for what it entails,” then it follows that the wording could not be an indicator by its inclusive (taḍammunī) or its implicative (iltizāmī) meaning — although the wording may indeed be an indicator for these two."},
    {"type": "pair",
     "ar": "فالأولى أن يقال في تفسير القرينة: هي الأمر الدال على الشيء من غير الاستعمال فيه.",
     "en": "So the preferable [way] of explaining the “indicator” is to say: it is the thing that indicates something without [the wording’s] being used for it."},
]
